import os
import platform
import subprocess
from argparse import ArgumentParser, RawTextHelpFormatter

import toml

from ntfyme.cmd.cmd_direct import direct_exec
from ntfyme.cmd.cmd_pipe import pipe_exec
from ntfyme.manager.encrypt import encrypt
from ntfyme.manager.setup_interaction import setup
from ntfyme.notification import notify
from ntfyme.utils.log.log import log_add


def main():
    """
    -> Handles the flags and errors
    -> calls functions based on the flags

    Arguments:
        None: Assumes the user wants to run the main command through pipe
        --cmd or -c : Input the command to cli as 'ntfyme --cmd <command>'
        --enc or -e : Encrypt password with your key for safety
        --log : The command log of ntfyme
        --config: The configuration file of ntfyme

        --help or -h : Shows the help message
        --version or -v : Shows the version of the program
    """

    parser = ArgumentParser(description="ntfyme")
    parser = ArgumentParser(
        description="""ntfyme is a simple notification tool to notify yourself when a long running process ends with local ping, gmail, telegram, etc. For setup guidelines or if you are facing any issue, checkout the official github repository at: https://github.com/AnirudhG07/ntfyme.""",
        formatter_class=RawTextHelpFormatter,
    )
    parser.add_argument("--version", "-v", action="version", version="ntfyme v0.0.1")
    parser.add_argument("--cmd", "-c", help="Run the command through direct execution")
    parser.add_argument(
        "--log", "-l", action="store_true", help="The command log of ntfyme"
    )
    parser.add_argument(
        "--config", action="store_true", help="The configuration file of ntfyme"
    )
    parser.add_argument(
        "--enc",
        "-e",
        action="store_true",
        help="Encrypting password through ntfyme_key",
    )
    parser.add_argument(
        "--interactive-setup",
        "-i",
        action="store_true",
        help="Interactively setup your notification configuration",
    )
    parser.add_argument(
        "--track-process",
        "-t",
        action="store_true",
        help="Track the process for suspensions and terminate if stalled for a long time",
    )

    args = parser.parse_args()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "config.toml")
    with open(config_path, "r") as file:
        config = toml.load(file)

    log_pager = config["ntfyme"]["log_pager"]
    terminal_print = config["ntfyme"]["terminal_print"]

    # Handling log and config arguments
    if args.log:
        log_path = os.path.join(script_dir, "utils", "log", "ntfyme.log")
        try:
            subprocess.run([log_pager, log_path])
        except Exception as e:
            print(f"Error occurred in opening log file. Error: {e}")
        return 0

    if args.config:
        config_path = os.path.join(script_dir, "config.toml")
        editor = os.getenv("EDITOR", "nano")  # Default to nano if EDITOR is not set
        # Open the config.toml file in the editor
        if platform.system() != "Windows":
            print(
                "For security reasons, please provide your sudo password to edit the config file."
            )
            subprocess.run(["sudo", editor, config_path])
            return 0
        subprocess.run([editor, config_path])
        return 0

    if args.enc:
        print(
            "Please provide your ntfyme_key for encrypting your password. This key is same throughout ntfyme. Whataver output you get will be based on the same key, please be mindful of the usage."
        )
        key = input("Enter your ntfyme_key: ")
        password = input("Enter your password: ")
        encrypted_password = encrypt(password, key)
        print(f"Encrypted password: {encrypted_password}")
        return 0

    if args.interactive_setup:
        setup()
        return 0

    results, key = None, None
    log_info = {}

    log_info["key"]=0
    if config["mail"]["enabled"] == "on":
        key = input("Enter your ntfyme_key: ")
        if not key:
            log_info["key"] = "1"


    if args.track_process:
        track_process = "on"
        log_info["track_process"] = "0"
    else:
        track_process = "off"
        log_info["track_process"] = "1"

    try:
        if args.cmd:
            results = direct_exec(args.cmd, terminal_print, track_process)
            log_info["execution"] = ": Direct :: 0"
        else:
            results = pipe_exec(terminal_print, track_process)
            log_info["execution"] = ": Pipe :: 0"

    except Exception as e:
        print(f"Error occurred in command execution. Error: {e}")
        log_info["error"] = "Execution: 1"

    try:
        notify(results, key)
        log_info["notify"] = "0"
    except Exception as e:
        print(f"Error occurred in notification. Error: {e}")
        log_info["notify"] = "1"

    log_add(results, log_info)
    return 0


if __name__ == "__main__":
    main()
