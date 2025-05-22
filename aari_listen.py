"""Placeholder for Aari's listening capabilities."""

import time


def listen_loop():
    print("[Aari] Lausche... (Platzhalter)")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("[Aari] Lauschen beendet.")


if __name__ == "__main__":
    listen_loop()
