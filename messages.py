MESSAGES = {
    "de": {
        "voice_engine_ready": "[Aari] Sprachengine bereit.",
        "say_voice_ready": "Meine Stimme ist bereit",
        "voice_failure": "[Aari] Meine Stimme funktioniert nicht: {err}",
        "installing_pyttsx3": "[Aari] Versuche pyttsx3 zu installieren...",
        "voice_output_unavailable": "[Aari] Sprachausgabe nicht verf\u00fcgbar.",
        "system_ready": "[Aari] System bereit."
    },
    "berndeutsch": {
        "voice_engine_ready": "[Aari] Stimm-Engine parat.",
        "say_voice_ready": "Mini Stimm isch parat",
        "voice_failure": "[Aari] Mini Stimm funktioniert nid: {err}",
        "installing_pyttsx3": "[Aari] Versuche pyttsx3 z'installiere...",
        "voice_output_unavailable": "[Aari] Sprachausgab n\u00f6d verf\u00fcgbar.",
        "system_ready": "[Aari] System parat."
    },
    "en": {
        "voice_engine_ready": "[Aari] Voice engine ready.",
        "say_voice_ready": "My voice is ready",
        "voice_failure": "[Aari] My voice doesn't work: {err}",
        "installing_pyttsx3": "[Aari] Trying to install pyttsx3...",
        "voice_output_unavailable": "[Aari] Voice output unavailable.",
        "system_ready": "[Aari] System ready."
    }
}

BASE_LANG = "de"


def get_message(key, lang=None):
    lang = lang or BASE_LANG
    if lang in MESSAGES and key in MESSAGES[lang]:
        return MESSAGES[lang][key]
    return MESSAGES[BASE_LANG].get(key, "")
