# Mise en mode examen d'une machine


1. Se connecter en mode administrateur. Restriction d'accès aux fichiers des autres utilisateurs
```sh
cd /home
sudo chmod go-rwx *
```

2. Création de l'utilisateur `examen` avec le mot de passe `examen`
```sh
sudo adduser examen
```

3. Se déconnecter, et se reconnecter sous le nom de login `examen`

4. Lancer Vs Code et installer l'extension python

5. Supprimer tous les dossiers du répertoire personnel et créer les dossiers`Travail` et `Sauvegarde` pour l'utilisateur `examen` :
```sh
rmdir *
mkdir Travail Sauvegarde
```

6. Créer le dossier `Sujets` en mode root :
```sh
sudo mkdir Sujets
```

7. En mode root, copier les sujets dans le dossier `Sujets`, les sujets sont téléchargeables ci-dessous
{{telecharger("Sujets épreuve blanche","../evaluations/EP blanches/Code-ex2.zip")}}

8. Changer les droits d'accès sur `Sauvegarde`
```sh
chmod a-rwx Sauvegarde 
```

9. Créer un script de copie des fichiers et de nettoyage lors de la déconnexion
Le gestionnaire de connection est `gdm3`, le script de déconnexion est `/etc/gdm3/PostSession/Default/`. Il faut donc éditer ce fichier et modifier le contenu :
```sh
sudo gedit /etc/gdm3/PostSession/Default/
```
Nouveau contenu :
```python
    #!/usr/bin/python3
    from os import path,mkdir,chmod
    import shutil

    SOURCE = "/home/exam/Travail/"
    PREFIXE = "/home/exam/Sauvegarde"

    def get_destination():
        num = 1
        dest = f"/home/exam/Sauvegarde/Session{num}/"
        while path.exists(dest):
            num += 1
            dest = f"/home/exam/Sauvegarde/Session{num}/"
        return dest

    chmod(PREFIXE,0o777)
    destination = get_destination()
    shutil.copytree(SOURCE,destination)
    shutil.rmtree(SOURCE)
    mkdir("/home/exam/Travail")
    chmod(PREFIXE,0o000)
```

10. Suppression de l'accès réseau sur la machine
```sh
sudo ifconfig enp3s0 down
```