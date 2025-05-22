import sys
import builtins
import os
import types

import pytest

import aari


def test_check_pyttsx3_success(monkeypatch):
    dummy_module = types.ModuleType("pyttsx3")
    monkeypatch.setitem(sys.modules, "pyttsx3", dummy_module)
    ok, err = aari.check_pyttsx3()
    assert ok is True
    assert err is None
    monkeypatch.delitem(sys.modules, "pyttsx3", raising=False)


def test_check_pyttsx3_failure(monkeypatch):
    def fake_import(name, *args, **kwargs):
        if name == "pyttsx3":
            raise ImportError("No module named pyttsx3")
        return orig_import(name, *args, **kwargs)

    orig_import = builtins.__import__
    monkeypatch.setattr(builtins, "__import__", fake_import)
    ok, err = aari.check_pyttsx3()
    assert ok is False
    assert "pyttsx3" in err
    monkeypatch.setattr(builtins, "__import__", orig_import)


def test_perform_self_check_success(monkeypatch, capsys):
    monkeypatch.setattr(aari, "check_pyttsx3", lambda: (True, None))
    called = []

    def fake_say(text, lang):
        called.append((text, lang))
    monkeypatch.setattr(aari, "say", fake_say)

    aari.perform_self_check("en")
    out = capsys.readouterr().out
    assert "[Aari] Voice engine ready." in out
    assert called == [("My voice is ready", "en")]


def test_perform_self_check_failure(monkeypatch, capsys):
    monkeypatch.setattr(aari, "check_pyttsx3", lambda: (False, "error"))
    executed = []

    def fake_system(cmd):
        executed.append(cmd)
        return 0

    monkeypatch.setattr(os, "system", fake_system)

    aari.perform_self_check("en")
    out = capsys.readouterr().out
    assert "[Aari] My voice doesn't work: error" in out
    assert "[Aari] Trying to install pyttsx3..." in out
    assert executed == ["pip install pyttsx3"]
