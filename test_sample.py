import pytest

def test_basic():
    assert 1 == 1

def test_math():
    assert 2 + 2 == 4

def test_string():
    assert "devops".upper() == "DEVOPS"

def test_list():
    assert len([1,2,3]) == 3

def test_true():
    assert True
