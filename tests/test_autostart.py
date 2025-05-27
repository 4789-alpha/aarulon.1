import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import setup_autostart


def test_generate_service_text():
    text = setup_autostart.generate_service_text("/usr/bin/python3", "/tmp/cli.py")
    assert "ExecStart=/usr/bin/python3 /tmp/cli.py listen" in text


def test_install_service(tmp_path, monkeypatch):
    monkeypatch.setattr(Path, "home", lambda: tmp_path)
    path = setup_autostart.install_service()
    assert path.exists()
    content = path.read_text()
    assert "Aari Host Service" in content
