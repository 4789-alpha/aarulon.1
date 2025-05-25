import os
import sys
import subprocess
import platform

REQUIREMENTS_FILE = "requirements.txt"


def install_requirements():
    """Install required packages using pip."""
    if os.path.isfile(REQUIREMENTS_FILE):
        print("Installing dependencies...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", REQUIREMENTS_FILE])
            return True
        except Exception as e:  # pragma: no cover - external dependency
            print("Failed to install dependencies:", e)
            return False
    # fallback: install pyttsx3 only
    try:
        import pyttsx3  # noqa: F401
        return True
    except Exception:
        print("Installing pyttsx3...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyttsx3"])
            return True
        except Exception as e:  # pragma: no cover - external dependency
            print("Failed to install pyttsx3:", e)
            return False


def main():
    print("=== Aari Installer ===")
    print(f"Detected platform: {platform.system()}")

    if not install_requirements():
        print("Please install the requirements manually and rerun this script.")
        input("Press Enter to exit...")
        return

    print("Dependencies installed.")
    print("Starting Aari...")

    # Start the main Aari script
    try:
        subprocess.check_call([sys.executable, "aari.py"])
    except Exception as e:
        print("Failed to start Aari:", e)

    # keep window open on double click
    input("\nFinished. Press Enter to exit...")


if __name__ == "__main__":
    main()
