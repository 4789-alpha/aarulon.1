import os
import sys
import subprocess
import platform


def install_pyttsx3():
    """Install the pyttsx3 package using pip."""
    try:
        import pyttsx3  # noqa: F401
        return True
    except Exception:
        pass

    print("Installing pyttsx3...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyttsx3"])
        return True
    except Exception as e:
        print("Failed to install pyttsx3:", e)
        return False


def main():
    print("=== Aari Installer ===")
    print(f"Detected platform: {platform.system()}")

    if not install_pyttsx3():
        print("Please install pyttsx3 manually and rerun this script.")
        input("Press Enter to exit...")
        return

    print("pyttsx3 installed.")
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
