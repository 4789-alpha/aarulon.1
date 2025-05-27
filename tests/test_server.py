import sys
from pathlib import Path
import threading
import socket
import urllib.request

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import aari_server


def run_temp_server():
    sock = socket.socket()
    sock.bind(("127.0.0.1", 0))
    port = sock.getsockname()[1]
    sock.close()
    thread = threading.Thread(target=aari_server.run_server, kwargs={"host": "127.0.0.1", "port": port}, daemon=True)
    thread.start()
    # wait for server to listen
    for _ in range(10):
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.1):
                break
        except OSError:
            pass
    return port


def test_server_ping():
    port = run_temp_server()
    with urllib.request.urlopen(f"http://127.0.0.1:{port}/ping") as resp:
        assert resp.read() == b"pong"


def test_server_say_invalid_signature():
    port = run_temp_server()
    try:
        urllib.request.urlopen(f"http://127.0.0.1:{port}/say?text=hi&signature=bad")
    except Exception as e:
        assert "403" in str(e)
