hide: - navigation in projets.md
# Projets

Le programme officiel de l'enseignement de spécialité {{ sc("nsi")}} précise que :
> *"Un quart au moins de l’horaire total de la spécialité est réservé à la conception et à
l’élaboration de projets conduits par les élèves.
Les projets réalisés par les élèves, sous la conduite du professeur, constituent un
apprentissage fondamental tant pour l’appropriation des concepts informatiques que pour
l’acquisition de compétences.*"

!!! Remarques général
    * Un **travail régulier** et des **efforts soutenus** sont donc attendus sur la réalisation des projets.
    * Les projets donnent lieu a une restitution sous forme de présentation orale devant la classe.
    
## Premier projet

### Projet 1 : Algorithmes de tri

#### Descriptif
Le but du projet est de revenir sur les algorithmes de tru vus en classe de première et d'en découvrir d'autres (notamment des algorithmes récursifs). Des comparaisons seront établis sur ces divers algorithmes (complexité).

#### Critère de réussites
* **[2 pts]** Savoir expliquer l'algorithme du tri par sélection. Ecrire une implémentation de cet algorithme en Python.
* **[2 pts]** Savoir expliquer l'algorithme du tri par insertion. Ecrire une implémentation de cet algorithme en Python.
* **[4 pts]** Faire des recherches sur le *tri à bulles*, en présenter le principe en montrant un exemple. Ecrire et tester une implémentation en Python.
* **[8 pts]** Faire des recherches sur le *tri fusion*, en présenter le principe en montrant un exemple. Ecrire et tester une implémentation en Python (avec la récursivité).
* **[4 pts]** Faire une synthèse comparative des ces algorithmes de tri.
* **[Bonus]** Présenter d'autres algorithmes de tri (par exemple le *quicksort*).

### Projet 2 : Programmer un jeu avec une interface graphique

#### Descriptif
Le but du projet est de programmer un jeu en Python avec une interface graphique. On privilégiera l'utilisation du module `turtle` de Python pour l'interface graphique. Les autres possibilités (notamment le module `tkinter`) sont déconseillées pour le moment. Les interactions avec l'utilisateur se feront via la saisie de chaîne de caractères (`textinput` de `turtle`) ou via la gestion d'événements dans la fenêtre `turtle`. 

!!! Attention
    Les critères de réussite pour ce projet sont donnés pour le jeu [Othello](https://fr.wikipedia.org/wiki/Othello_(jeu)){target=_blank}. Les critères de réussite seront adaptés si un autre jeu est proposé. A titre d'exemples, on peut programmer les jeux suivants : Dames, Puissance4, Démineur, Mastermind, Pong, Snake, Casse-brique, ...

#### Critères de réussites

* **[2 pts]** Faire des recherches sur le jeu, en avoir compris les règles et savoir les présenter. 
* **[4 pts]** Mettre en place une représentation interne à Python du plateau de jeu et pouvoir l'afficher.
* **[4 pts]** Vérifier qu'un coup proposé par le joueur est valide, modifier le contenu du plateau de jeu en conséquence. A ce stade du projet, une partie est déjà possible entre deux joueurs humains.
* **[4 pts]** Intégrer la possibilité de sauvegarder une partie en cours. Il faut donc décider d'une représentation sous forme de fichier texte d'une partie (état du plateau, nom des joueurs, ...).
* **[6 pts]** Intégrer la possibilité de jouer contre l'ordinateur en programmant une stratégie pour lui. La plus simple étant que l'ordinateur joue le coup qui retourne le maximum de disque en sa faveur.
* **[Bonus]** Rajouter des options aux jeu (chronomètre, couleurs, aspect graphique du plateau, sons, ...). Programmer plusieurs stratégies de jeu pour l'ordinateur.
--8<-- "includes/glossaire.md"

### Projet 3 : Programmer un traceur de fonctions

#### Descriptif
Le but de ce projet est de programmer un *traceur de fonctions* comme sur les calculatrices graphiques en utilisant le module `turtle`. Comme sur une calculatrice, on proposera :

* une touche <span class='encadre'>$f(x)$</span> permettant d'entrer l'expression des fonctions,
* une touche <span class='encadre'>fenêtre</span> permettant de définir le repère,
* une touche <span class='encadre'>graph</span> permettant de tracer et de visualiser le graphique.

#### Critères de réussites
* **[4 pts]** Pouvoir entrer une fonction sous la forme d'une chaîne de caractères et l'évaluer (penser à utiliser la fonction `eval` de Python). Faire un prétraitement de l'expression de la fonction afin de signaler une erreur éventuelle à l'utilisateur (erreur de parenthésage par exemple).
* **[4 pts]** Pouvoir définir un repère et le tracer à l'aide de `turtle`. Attention ici à faire correspondre la taille de la fenêtre graphique avec les dimensions du repère donné par l'utilisateur.
* **[4 pts]** Ecrire la partie permettant de tracer les fonctions. Attention au domaine de définition de la fonction.
* **[4 pts]** Ajouter des fonctionnalités annexes (couleurs, épaisseurs et style des traits, graduations, ...)
* **[4 pts]** Intégrer la possibilité d'effectuer des lectures graphiques en affichant par exemple l'abscisse et l'ordonnée d'un point quelconque de la courbe.
* **[Bonus]** Intégrer des fonctionnalités comme le zoom sur une partie du graphique 

### Projet 4 : Résoudre le problème des huit reines

#### Descriptif
Le but du projet est d'écrire un programme permettant de résoudre le [problème des huit reines (ou dames)](https://fr.wikipedia.org/wiki/Probl%C3%A8me_des_huit_dames){target=_blank}. Ce problème est un grand classique de la programmation récursive. Dans ce projet, on s'intéresse aussi à la réalisation d'une sortie graphique (avec `turtle`) et à la possibilité de rechercher à la main des solutions en s'aidant de cette interface.

#### Critères de réussites
* **[4 pts]** Comprendre le problème, savoir indiquer si une configuration est ou non une solution. Savoir rechercher à la main une solution au problème.
* **[4 pts]** Réaliser l'interface graphique permettant de représenter l'échiquier et les dames.
* **[2 pts]** Réaliser une interface permettant de placer les reines en indiquant au fur et à mesure du placement les places encores disponibles pour une reine.
* **[2 pts]** Faire des recherches sur un algorithme récursif appelé *backtracking* qui permet de résoudre efficacement ce problème. On pourra par exemple consulter [ce site](https://interstices.info/le-probleme-des-8-reines/){target=_blank}
* **[6 pts]** Programmer cet algorithme pour donner les 92 solutions du problème.
* **[2 pts]** Accélérer votre algorithme en tenant compte des symétries du problème.
* **[Bonus]** Résoudre par le même procédé un problème similaire, par exemple le [problème du cavalier](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_cavalier){target=_blank}

### Projet 5 : Programmer le jeu de la vie

#### Descriptif
Le but du projet est de réaliser une interface graphique permettant de visualiser les étapes du [**jeu de la vie**](https://fr.wikipedia.org/wiki/Jeu_de_la_vie){target=_blank}. Afin de simplifier le problème, on supposera dans un premier temps que le plateau de jeu est limité en taille.


#### Critères de réussites
* **[2 pts]** Avoir compris et pouvoir expliquer les règles du jeu de la vie. Savoir prédire l'évolution d'une configuration simple.
* **[4 pts]** Réaliser l'interface graphique permettant de visualiser une configuration.
* **[6 pts]** Programmer l'évolution d'une configuration et sa visualisation à chaque étape.
* **[2 pts]** Intégrer des options de couleurs pour les cellules (par exemple sur la page wikipedia, les cellules bleues sont en cours de vie, les vertes naissent, les rouges meurent ...)
* **[2 pts]** Améliorer l'interface de façon à pouvoir rapidement intégrer des motifs classiques (oscillateurs, vaisseaux, ...) et suivre leur évolution
* **[4 pts]** Ajouter la possibilité de sauvegarder un motif sous la forme d'un fichier texte et donc de charger un motif lu dans un fichier texte externe.
* **[Bonus]** Reproduire l'évolution des motifs de la page wikipedia à l'aide de votre programme.

### Projet 6 :  Projet libre

#### Descriptif 
Projet libre au choix de l'élève mais soumis à la validation préalable de l'enseignant.

#### Critères de réussite
Les critères de réussites seront établis avec l'élève en fonction du projet choisi.