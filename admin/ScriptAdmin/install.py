#!/usr/bin/env python3

import paramiko
from getpass import getpass

HOSTNAME = ["adalovelace","kenthomson","dennisritchie","georgeboole","linustordvalds","edgarcodd","johnvonneumann","gracehooper","blaisepascal","timbernerslee","guidovanrossum","francesallen"]
NBHOST = len(HOSTNAME)
USERNAME = "administrateur"
PROXY = "172.19.240.1:3129"
PROXY_USER = "fabrice.nativel"

INST = { 1 : "pip", 2 : "snap", 3 : "apt-get"}

# initilisation du client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print(f'===== Installation automatique sur {NBHOST} machines =====')
# Selection type d'installation (apt, snap ou pip)
print("Type d'installation : ")
for i in INST:
    print(f'{i}) : {INST[i]}')
type_inst = int(input("Type d'installation : "))
paq = input("Nom des paquets/logiciels à installer : ")
# Mise en place lorsque necessaire (pip ou snap)
if type_inst == 1 or type_inst==2:
    print("Identification proxy requise pour ce type d'installation")
    proxy_password = getpass("Entrer le mot de passe du proxy : ")
    if type_inst == 1:
        # Installation d'un pip, le proxy est indiqué dans la commande
        proxy=f"https://{PROXY_USER}:{proxy_password}@{PROXY}"
        todo = [f"sudo -S pip3 install --proxy={proxy} {paq}"]
    else:
        # Installation d'un snap, il faut déclarer le proxy puis l'enlever
        proxy="http://"+PROXY_USER+":"+proxy_password+"@"+PROXY
        todo = [f'sudo -S snap set system proxy.https="{proxy}"']
        todo.append(f'sudo -S snap install {paq}')
        todo.append('sudo -S snap set system proxy=""')
else:
    todo = [f'sudo -S apt-get -q -y install {paq}']
password = getpass("Entrer le mot de passe sudo : ")
# Exécution de la commande d'installation sur toutes les machines
for h in HOSTNAME:
    try:
        host = h+".local"
        print(f'> Tentative de connection sur {h}')
        client.connect(hostname=host,username=USERNAME,password=password)
        print(f'> Connection établie sur {h}')
        print(f"> Lancement de l'installation de {paq} via {INST[type_inst]}")
        for op in todo:
            # Les commandes sudo necessitent un mot de passe qui est entré de façon automatique
            stdin, stdout, stderr = client.exec_command(op)
            stdin.write(password)
            stdin.write('\n')
            stdin.flush()
            err = stderr.read().decode()
            if err:
                print(err)
        print(f'> Installation effectuée sur {h}')
    except:
        print(f'* Erreur : connection refusée sur {h}')
print('===== Fin =====')
