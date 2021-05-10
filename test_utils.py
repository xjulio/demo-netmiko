import utils
import netmiko

csv1 = "test/devices1.txt"
csv2 = "test/devices2.txt"
csv3 = "test/devices3.txt"

def test_load_csv1():
    devices = utils.load_csv(csv1)
    assert len(devices) == 3

def test_load_csv2():
    devices = utils.load_csv(csv1)
    assert len(devices) == 3    