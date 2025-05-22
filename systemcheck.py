"""Einfache Systemprüfungen für Aari."""

import shutil
import subprocess


def check_command(cmd):
    """Return True if command exists."""
    return shutil.which(cmd) is not None


def ffmpeg_version():
    try:
        output = subprocess.check_output(["ffmpeg", "-version"], stderr=subprocess.STDOUT)
        return output.decode().splitlines()[0]
    except Exception:
        return None


if __name__ == "__main__":
    print("ffmpeg verfügbar:", check_command("ffmpeg"))
    print("ffmpeg Version:", ffmpeg_version())
