"""Offline Speech-to-Text with Vosk."""

import json
import os
import queue

try:
    import sounddevice as sd
    from vosk import Model, KaldiRecognizer
except Exception as e:  # pragma: no cover - dependency missing in tests
    sd = None
    Model = None
    KaldiRecognizer = None
    _import_error = e
else:
    _import_error = None

from messages import BASE_LANG


def forward_to_aari(text):
    """Send recognized ``text`` to the main controller."""
    try:
        import aari
        lang = aari.load_config().get("language", BASE_LANG)
        aari.handle_voice_command(text, lang)
    except Exception as exc:  # pragma: no cover - controller not available
        print(f"[Aari] Fehler beim Weiterleiten: {exc}")


def listen_loop(model_path="model"):
    """Listen continuously and forward recognized phrases."""
    if _import_error:
        print(f"[Aari] Spracherkennung nicht verf\u00fcgbar: {_import_error}")
        return

    if not os.path.isdir(model_path):
        print(f"[Aari] Vosk-Modell nicht gefunden: {model_path}")
        return

    model = Model(model_path)
    recognizer = KaldiRecognizer(model, 16000)
    audio_queue = queue.Queue()

    def callback(indata, frames, time_info, status):  # pragma: no cover - realtime
        if status:
            print(status)
        audio_queue.put(bytes(indata))

    print("[Aari] Lausche...")
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype="int16",
                           channels=1, callback=callback):
        try:
            while True:
                data = audio_queue.get()
                if recognizer.AcceptWaveform(data):
                    result = json.loads(recognizer.Result())
                    text = result.get("text", "").strip()
                    if text:
                        forward_to_aari(text)
        except KeyboardInterrupt:
            print("[Aari] Lauschen beendet.")


if __name__ == "__main__":
    listen_loop()
