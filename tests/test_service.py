import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import greet, add, multiply


def test_greet():
    assert greet() == 'Hello, World!'
    assert greet('Python') == 'Hello, Python!'


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(50, 50) == 100


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 5) == 0
    assert multiply(5, 5) == 25

