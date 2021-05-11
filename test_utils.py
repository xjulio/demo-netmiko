import utils
import pytest

csv1 = "test/devices1.txt"
csv2 = "test/devices2.txt"
csv3 = "test/devices3.txt"

def test_load_csv1():
    devices = utils.load_csv(csv1)
    assert len(devices) == 3
    assert devices[0].ip == "192.168.0.254"
    assert devices[1].ip == "192.168.0.253"
    assert devices[2].ip == "192.168.0.252"
    
    assert devices[0].password == "cisco"

def test_load_csv2():
    with pytest.raises(AttributeError):
        devices = utils.load_csv(csv2)

def test_load_csv3():
    devices = utils.load_csv(csv3)
    assert len(devices) == 2
    assert devices[0].ip == "192.168.0.253"
    assert devices[1].ip == "192.168.0.200"
    # testano se a senah esta em branco
    assert devices[1].password == ""
