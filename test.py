import pytest
from teste import somar
from teste import subtrair

def test_somar():
    """docstring for test_somar"""
    assert somar(2,4) == 5

def test_subtrair():
    """docstring for test_somar"""
    assert subtrair(2,4) == -2