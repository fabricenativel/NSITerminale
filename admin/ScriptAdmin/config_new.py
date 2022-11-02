#!/usr/bin/env python3

import paramiko
from getpass import getpass

USERNAME = "administrateur"
PROXY = "172.19.240.1:3129"
PROXY_USER = "fabrice.nativel"

## Définition ici des paquets à installer lors de la configuration initiale d'un post
PAQUETS_APT = ["net_tools","traceroute","python3-tk","veyon-master","htop","sqlite3","sqlitebrowser","graphviz","vlc"]
PAQUETS_PIP = ["jupyterlab","pylint","matplotlib","Image","graphviz","pygames"]
PAQUETS_SNAP = ["code"]

host = input("Nom du nouveau poste à configurer :")
h=host+".local"
password = getpass("Entrer le mot de passe sudo : ")
proxy_password = getpass("Entrer le mot de passe du proxy : ")


## Génération de la liste des commandes à exécuter 
todo = []
# Pour les paquets apt
for paq in PAQUETS_APT:
    todo.append(f'sudo -S apt-get -q -y install {paq}')
# Pour les paquets pip, le proxy apparaît comme option de la commande
proxy=f"https://{PROXY_USER}:{proxy_password}@{PROXY}"
for paq in PAQUETS_PIP:
    todo.append(f"sudo -S pip3 install --proxy={proxy} {paq}")
# Pour les commandes snap, il faut mettre en place le proxy puis l'enlever
proxy="http://"+PROXY_USER+":"+proxy_password+"@"+PROXY
todo.append(f'sudo -S snap set system proxy.https="{proxy}"')
for paq in PAQUETS_SNAP:
    todo.append(f'sudo -S snap install --classic {paq}')
todo.append('sudo -S snap set system proxy=""')

# initilisation du client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Exécution des commandes de configuration 
try:
    print(f'> Tentative de connection sur {h}')
    client.connect(hostname=h,username=USERNAME,password=password)
    print(f'> Connection établie sur {h}')
    print("> Lancement de la configuration de base")
    for op in todo:
        # Les commandes sudo necessitent un mot de passe qui est entré de façon automatique
        print(f'>Exécution de : {op}')
        stdin, stdout, stderr = client.exec_command(op)
        stdin.write(password)
        stdin.write('\n')
        stdin.flush()
        err = stderr.read().decode()
        if err:
            print(err)
    print(f'> Installation effectuée sur {host}')
except:
    print(f'* Erreur : connection refusée sur {host}')
