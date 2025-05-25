import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import aari
import aari_listen
from cli import main


def test_cli_self_check(monkeypatch):
    called = []
    monkeypatch.setattr(aari, "load_config", lambda: {"language": "en"})
    monkeypatch.setattr(aari, "perform_self_check", lambda lang: called.append(lang))
    main(["self-check"])
    assert called == ["en"]


def test_cli_system_data(monkeypatch):
    called = []
    monkeypatch.setattr(aari, "display_system_data", lambda: called.append(True))
    main(["system-data"])
    assert called == [True]


def test_cli_listen(monkeypatch):
    called = []
    monkeypatch.setattr(aari_listen, "listen_loop", lambda: called.append(True))
    main(["listen"])
    assert called == [True]


def test_cli_say(monkeypatch):
    called = []
    monkeypatch.setattr(aari, "load_config", lambda: {"language": "en"})
    monkeypatch.setattr(aari, "say", lambda text, lang: called.append((text, lang)))
    main(["say", "hi"])
    assert called == [("hi", "en")]


def test_cli_no_args(capsys):
    main([])
    out = capsys.readouterr().out
    assert "usage:" in out

