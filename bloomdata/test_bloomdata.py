import pytest 
import bloomdata.bloomdata as bd

def test_increment_int():
    assert bd.increment(3) == 4
    assert bd.increment(-2) == -1

def test_increment_float():
    assert bd.increment(2.4) == 3.4 