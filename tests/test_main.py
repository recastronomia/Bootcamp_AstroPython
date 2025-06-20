import pytest
from src.main import get_phrase

def test_get_phrase():
    expected = "La RECA la construímos entre todos"
    assert get_phrase() == expected