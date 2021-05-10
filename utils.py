import os
import netmiko
from devices import Device


def load_csv(csv_filename:str) -> list[Device]:
    devices = []
    if not os.path.exists(csv_filename):
        raise FileNotFoundError("Arquivo não existe no sistema de arquivos!")

    with open(csv_filename, "r") as fp:
        line = fp.readline()

        while line:
            # ip, user, password
            line = line.rstrip()
            line_array = line.split(",")
            device = Device(ip=line_array[0], user=line_array[1], password=line_array[2])
            devices.append(device)
            # read next line
            line = fp.readline()

    return devices;