import os
import subprocess

import toml


def linux_config():
    current_dir = os.path.dirname(__file__)
    package_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
    config_path = os.path.join(package_root, "config.toml")

    with open(config_path, "r") as f:
        conf = toml.load(f)
    enabled = conf["local"]["enabled"]
    success_sub = conf["ntfyme"]["success_subject"]
    error_sub = conf["ntfyme"]["error_subject"]

    return {
        "enabled": enabled,
        "success_sub": success_sub,
        "error_sub": error_sub,
    }


def notify_linux(results):
    """
    Linux uses notify-send as default tool. This will be used for linux local notifications
    """
    configs = linux_config()

    if not configs["enabled"] == "on":
        return

    success_sub = configs["success_sub"]
    error_sub = configs["error_sub"]
    pid = results["pid"]
    error = results["error"]

    try:
        if error == "none":
            subprocess.run(
                [
                    "notify-send",
                    f"ntfyme :: {success_sub}",
                    f"Process {pid} has ended successfully.",
                ]
            )
            return 0
        subprocess.run(
            [
                "notify-send",
                f"ntfyme :: {error_sub}",
                f"Process {pid} ended with a failure.",
            ]
        )
        return 0
    except Exception as e:
        subprocess.run(
            [
                "notify-send",
                "ntfyme: Notification error",
                f"Error {e} occurred in processing your notification request",
            ]
        )
        return 1
