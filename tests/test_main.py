import pytest
from src.main import get_phrase

def test_get_phrase():
    expected = "La RECA la construímos entre todos, todas y todxs para la comunidad de Python en español, A este bootcamp asistieron Kevin,Diana,Alejandra,Edwin,Alexandra,Catalina,Mariana y Dayana "
    assert get_phrase() == expected