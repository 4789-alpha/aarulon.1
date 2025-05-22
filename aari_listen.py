"""Placeholder for Aari's listening capabilities."""

import time


def listen_loop():
    print("[Aari] Listening... (placeholder)")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("[Aari] Stopped listening.")


if __name__ == "__main__":
    listen_loop()
