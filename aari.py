import os
import json

from messages import get_message, BASE_LANG
from systemcheck import check_pyttsx3, get_system_data


def say(text, lang):
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception:
        print(get_message("voice_output_unavailable", lang))


def perform_self_check(lang):
    ok, err = check_pyttsx3()
    if ok:
        print(get_message("voice_engine_ready", lang))
        say(get_message("say_voice_ready", lang), lang)
    else:
        print(get_message("voice_failure", lang).format(err=err))
        print(get_message("installing_pyttsx3", lang))
        os.system("pip install pyttsx3")


def display_system_data():
    data = get_system_data()
    print("[Aari] Systemdaten:")
    for key, value in data.items():
        print(f"  {key}: {value}")


def load_config():
    try:
        with open("aari_config.json", "r") as f:
            return json.load(f)
    except Exception:
        return {}


def main():
    config = load_config()
    lang = config.get("language", BASE_LANG)
    display_system_data()
    perform_self_check(lang)
    # Placeholder for future modules
    print(get_message("system_ready", lang))


if __name__ == "__main__":
    main()
