import os
import sys
import json


def check_pyttsx3():
    try:
        import pyttsx3  # noqa: F401
        return True, None
    except Exception as e:
        return False, str(e)


def say(text):
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception:
        print("[Aari] Voice output unavailable.\n")


def perform_self_check():
    ok, err = check_pyttsx3()
    if ok:
        print("[Aari] Voice engine ready.")
        say("Mini Stimm isch parat")
    else:
        print("[Aari] Mini Stimm funktioniert nid: {}".format(err))
        print("[Aari] Versuche pyttsx3 zu installieren...")
        os.system("pip install pyttsx3")


def main():
    perform_self_check()
    # Placeholder for future modules
    print("[Aari] System ready.")


if __name__ == "__main__":
    main()
