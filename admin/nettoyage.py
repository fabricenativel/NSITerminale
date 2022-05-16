#!/usr/bin/python3
from os import path,mkdir,chmod
import subprocess
import shutil

SOURCE = "/home/examen/Travail"
PREFIXE = "/home/examen/Sauvegarde"

def get_destination():
    num = 1
    dest = f"{PREFIXE}/Session{num}/"
    while path.exists(dest):
        num += 1
        dest = f"{PREFIXE}/Session{num}/"
    return dest

user = subprocess.getoutput("whoami")
if user=="examen":
    chmod(PREFIXE,0o777)
    destination = get_destination()
    shutil.copytree(SOURCE,destination)
    shutil.rmtree(SOURCE)
    mkdir(SOURCE)
    chmod(PREFIXE,0o000)
