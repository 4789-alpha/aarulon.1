import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from messages import get_message


def test_get_message_default_lang():
    assert get_message("voice_engine_ready") == "[Aari] Sprachengine bereit."


def test_get_message_specific_lang():
    assert get_message("voice_engine_ready", lang="en") == "[Aari] Voice engine ready."


def test_get_message_fallback_to_base():
    # key exists only in base or fallback to base when language missing
    assert get_message("voice_engine_ready", lang="nonexistent") == "[Aari] Sprachengine bereit."


def test_get_message_unknown_key():
    assert get_message("unknown_key") == ""
