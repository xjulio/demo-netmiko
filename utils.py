import os
import ipaddress

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
            ip = line_array[0]
            user = line_array[1]
            
            try:
                password = line_array[2]
            except IndexError:
                password = ""

            try:
                ip_addr = ipaddress.IPv4Address(ip)
            except ipaddress.AddressValueError:
                raise AttributeError("Endereço IP invalido!")

            device = Device(ip=ip, user=user, password=password)
            devices.append(device)
            # read next line
            line = fp.readline()

    return devices;