# tests/test_core.py
from framework_package.core import greet

def test_greet():
    assert greet("Alice") == "Hello, Alice!"
