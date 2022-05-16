import paramiko
from scp import SCPClient
from getpass import getpass
import csv
import datetime

USERNAME = "administrateur"
ELEVES = "Eleves2021.csv"

def get_eleves(fichier):
    df = open(fichier,encoding="utf-8")
    eleves = list(csv.DictReader(df))
    df.close()
    return eleves

def get_groupe(eleve):
    groupe = []
    for e in eleves:
        if e["Groupe"] not in groupe:
            groupe.append(e["Groupe"])
    return groupe

print("*** Récupération d'un devoir ")
eleves = get_eleves(ELEVES)
groupes = get_groupe(eleves)
print("Liste des groupes disponibles :")
for i in range(len(groupes)):
    print(f"{i}) {groupes[i]} ")
num_gr = int(input("Numéro du groupe :"))
le_groupe = [e for e in eleves if e["Groupe"]==groupes[num_gr]]
num_devoir = int(input("Numéro du devoir à récupérer : "))
password = getpass("Entrer le mot de passe administrateur : ")
go = input("Entrer pour lancer la récupération du devoir")
temoin_recup="OK-"+datetime.datetime.now().strftime("%d%m%Y-%H:%M")
ft =open(temoin_recup,"w")
ft.close()

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
localname = f"/home/Administrateur/Evaluations/{groupes[num_gr]}/E{num_devoir}/"


for eleve in le_groupe:
    # Connection à la machine de l'élève
    client.connect(hostname=eleve["Ordinateur"]+'.local',username=USERNAME,password=password)
    # Transfert des fichiers en local
    with SCPClient(client.get_transport()) as scp:
        scp.get(f"/home/{eleve['identifiant']}/Evaluations/E{num_devoir}",localname+eleve["Nom Prénom"]+'/',recursive=True)
        scp.put(temoin_recup,f"/home/{eleve['identifiant']}/Evaluations/E{num_devoir}/")
    print(f"Transfert terminé pour {eleve['Nom Prénom']}")

print("Récupération terminé")
