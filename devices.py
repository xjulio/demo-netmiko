class Device:
    """Classe para respresentar um disposivo
    """
    def __init__(self, ip, user, password, hostname=None, mac=None, type=None):
        """Construtor

        Args:
            ip ([type]): [description]
            user ([type]): [description]
            password ([type]): [description]
            hostname ([type], optional): [description]. Defaults to None.
            mac ([type], optional): [description]. Defaults to None.
            type ([type], optional): [description]. Defaults to None.
        """
        self.hostname = hostname
        self.ip = ip
        self.user = user
        self.password = password
        self.mac = mac
        self.type = type

    def __str__(self) -> str:     
        return self.hostname + " " + self.ip + " " + self.mac

if __name__ == "__main__":
    raise NotImplementedError("Uso direto nao permitido, use a diretiva import!")

"""
lista = []
dic = {}
nome = "a"

router01
192.168.0.254
admin
cisco
c0:7b:bc:99:f7

sw01
192.168.0.253
admin
cisco123
c0:7b:bd:05:cb


user = (input("Digite seu Usuario:? "))
pswd = getpass.getpass() 
caixas = []

sn = 'yes'
c = 0
while sn == 'yes':
    c += 1
    caixas.append(input (f"Enter {c}° device IP: "))
    sn = input("Deseja um novo equipamento (yes/no): ")

while True:
    for i in caixas:
        print(i)
        LEGADO = {
            'device_type': 'cisco_nxos',
            'ip': i,
            'username': user,
            'password': pswd
            }
        net_connect = ConnectHandler(**LEGADO)  
        comandos = open("comandos.txt", "r").readlines()
        for cmd in comandos:
            with open(f"{i}.txt", "a") as file:
                file.write(cmd)
                file.write(net_connect.send_command(cmd))
                file.write("="*10)
        net_connect.disconnect()
    print ("="*20, "\n","\t","All done!","\n","="*20)
    break
"""