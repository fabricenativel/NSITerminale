#!/usr/bin/env python3

import paramiko
from getpass import getpass

HOSTNAME = ["adalovelace","kenthomson","dennisritchie","georgeboole","linustordvalds","edgarcodd","johnvonneumann","gracehooper","blaisepascal","timbernerslee","guidovanrossum","francesallen"]
NBHOST = len(HOSTNAME)
USERNAME = "administrateur"

OPERATIONS = ["sudo -S reboot"]

# initilisation du client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print(f'===== Reboot automatique sur {NBHOST} machines =====')

password = getpass("Entrer le mot de passe de connection : ")

for h in HOSTNAME:
    try:
        host = h+".local"
        print(f'> Tentative de connection sur {h}')
        client.connect(hostname=host,username=USERNAME,password=password)
        print(f'> Connection établie sur {h}')
        print('> Lancement du reboot')
        for op in OPERATIONS:
            stdin, stdout, stderr = client.exec_command(op)
            stdin.write(password)
            stdin.write('\n')
            stdin.flush()
            err = stderr.read().decode()
            if err:
                print(err)
        print(f'> Reboot effectué sur {h}')
    except:
        print(f'* Erreur : connection refusée sur {h}')
print('===== Fin =====')
