"""Einfache Systemprüfungen für Aari."""

import shutil
import subprocess
import platform


def check_command(cmd):
    """Return True if command exists."""
    return shutil.which(cmd) is not None


def ffmpeg_version():
    try:
        output = subprocess.check_output(["ffmpeg", "-version"], stderr=subprocess.STDOUT)
        return output.decode().splitlines()[0]
    except Exception:
        return None


def check_pyttsx3():
    """Check if pyttsx3 can be imported."""
    try:
        import pyttsx3  # noqa: F401
        return True, None
    except Exception as e:
        return False, str(e)


def check_audio_output():
    """Check if an audio output device is available via pyaudio."""
    try:
        import pyaudio
        pa = pyaudio.PyAudio()
        pa.get_default_output_device_info()
        pa.terminate()
        return True, None
    except Exception as e:
        return False, str(e)


def check_audio_input():
    """Check if an audio input device is available via pyaudio."""
    try:
        import pyaudio
        pa = pyaudio.PyAudio()
        pa.get_default_input_device_info()
        pa.terminate()
        return True, None
    except Exception as e:
        return False, str(e)


def get_system_data():
    """Collect basic system data used by Aari."""
    data = {
        "platform": platform.platform(),
        "python_version": platform.python_version(),
        "ffmpeg_available": check_command("ffmpeg"),
        "ffmpeg_version": ffmpeg_version(),
    }

    ok, err = check_pyttsx3()
    data["pyttsx3_available"] = ok
    data["pyttsx3_error"] = err

    ok, err = check_audio_output()
    data["audio_output_available"] = ok
    data["audio_output_error"] = err

    ok, err = check_audio_input()
    data["audio_input_available"] = ok
    data["audio_input_error"] = err

    return data


if __name__ == "__main__":
    data = get_system_data()
    for key, value in data.items():
        print(f"{key}: {value}")
