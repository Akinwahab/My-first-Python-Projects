from project import age, buddy_check, select_subject
import pytest


def test_age():
    assert age("I am 15") == "15"
    assert age("15 years old") == "15"
    with pytest.raises(ValueError):
        age("I am a boy")


def test_buddy_check():
    assert buddy_check("Yes") == "Akinwahab's Buddy"
    assert buddy_check("No") == "Not a buddy"
    assert buddy_check("Maybe") == "Not a buddy"


def test_select_subject_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "3")
    result = select_subject()
    assert result == "physics.json"
