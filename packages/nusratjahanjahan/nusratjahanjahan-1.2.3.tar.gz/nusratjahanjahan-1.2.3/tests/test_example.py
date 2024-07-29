# tests/test_example.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mypackage.example import add

def test_add():
    assert add(1, 2) == 3
