# tests/test_core.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from framework_package.core import greet

def test_greet():
    assert greet("Alice") == "Hello, Alice! Welcome to Framework Package."
    assert greet("Bob") == "Hello, Bob! Welcome to Framework Package."
