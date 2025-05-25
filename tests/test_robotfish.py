import pytest
import robotfish


def test_control_robot_fish_allows_signature(capsys):
    assert robotfish.control_robot_fish("swim", "4789") is True
    out = capsys.readouterr().out
    assert "robotfish --action swim" in out


def test_control_robot_fish_denies_signature():
    with pytest.raises(PermissionError):
        robotfish.control_robot_fish("swim", "0000")
