import os
import subprocess
import sys
import threading
import time

import toml

def remarks(return_code:int)->str:
    """
    Gives remarks based on the return code
    """
    return_code_remarks = {
    0: "Success. The command executed successfully without any errors.",
    1: "General error. The command failed due to a general error.",
    2: "Misuse of shell built-ins (according to Bash documentation).",
    126: "Command invoked cannot execute. This might happen if the command is not executable.",
    127: "Command not found. This indicates that the command was not found in the system's PATH.",
    128: "Invalid argument to exit. This indicates that the exit status is out of the range of valid exit statuses.",
    130: "Script terminated by Control-C. This indicates that the script was terminated by the user pressing Control-C.",
    137: "Command terminated by signal 9 (SIGKILL)."
    }
    return return_code_remarks.get(return_code, "Unknown return code")

class ProcessMonitor:
    def __init__(self, timeout, iterations):
        self.timeout = timeout
        self.iterations = iterations
        self.last_activity = time.time()
        self.lock = threading.Lock()
        self.stalled_count = 0

    def update_activity(self):
        with self.lock:
            self.last_activity = time.time()
            self.stalled_count = 0  # Reset stall count on activity

    def check_timeout(self):
        with self.lock:
            return time.time() - self.last_activity > self.timeout

    def increment_stalled_count(self):
        with self.lock:
            self.stalled_count += 1
            return self.stalled_count


def read_output(pipe, output_list, print_func, monitor=None):
    """Read lines or characters from a pipe and print them, storing them in a list."""
    while True:
        data = pipe.read(1)  # Read one character at a time
        if not data:
            break
        output_list.append(data)
        print_func(data, end="", flush=True)
        if monitor:
            monitor.update_activity()


def monitor_stall(monitor, process, check_interval):
    """Monitor for stalling and log an alert if detected."""
    while process.poll() is None:  # Continue while the process is running
        if monitor.check_timeout():
            stalled_count = monitor.increment_stalled_count()
            print(
                "Warning: Process may be stalled. No output for a while.",
                file=sys.stderr,
            )
            if stalled_count >= monitor.iterations:
                print("Error: Process output is stalled.", file=sys.stderr)
                process.terminate()  # Terminate the process
                break
        time.sleep(check_interval)  # Check every sleep_time seconds


def capture(cmd, track_process):

    config_path = os.path.join(os.path.dirname(__file__), "..", "config.toml")
    with open(config_path, "r") as f:
        config = toml.load(f)

    timeout = config["suspend"]["timeout"]
    iterations = config["suspend"]["iterations"]
    enabled = True if track_process == "on" else False
    check_interval = config["suspend"]["check_interval"]

    # Set the PYTHONUNBUFFERED environment variable to force unbuffered output
    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"

    monitor = ProcessMonitor(timeout, iterations) if enabled else None

    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        text=True,
        bufsize=0,
        env=env,
    )
    output, error = [], []

    stdout_thread = threading.Thread(
        target=read_output, args=(process.stdout, output, print, monitor)
    )
    stderr_thread = threading.Thread(
        target=read_output,
        args=(
            process.stderr,
            error,
            lambda x, **kwargs: None,  # Do nothing instead of printing
            monitor,
        ),
    )

    stdout_thread.start()
    stderr_thread.start()

    if enabled:
        stall_thread = threading.Thread(
            target=monitor_stall, args=(monitor, process, check_interval)
        )
        stall_thread.start()

    stdout_thread.join()
    stderr_thread.join()
    process.wait()

    if enabled:
        stall_thread.join()

    error_message = "".join(error)
    if enabled and monitor.stalled_count >= iterations:
        error_message += "Error: Process output is stalled."


    return {
        "output": "".join(output),
        "error": error_message,
        "pid": process.pid,
        "return_code": process.returncode,
    }
