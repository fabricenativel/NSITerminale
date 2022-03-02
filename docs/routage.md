
{% set num = 12 %}
{% set theme = "os" %}

{{ titre_chapitre(num,titre,theme)}}

!!! rappel
    Avant de commencer ce chapitre, revoir les notions de [réseau vues en classe de première](https://fabricenativel.github.io/NSIPremiere/reseau/){target = _blank}. En, particulier :
    * consulter l'activité 1 pour une initiation à l'utilisation du [logiciel de simulation de réseau filius](https://fabricenativel.github.io/NSIPremiere/reseau/#activite-1-simuler-un-reseau-avec-filius){target=_blank},
    * les notions d'adresses {{sc("ip")}},
    * le [diaporama de cours de ce chapitre](https://fabricenativel.github.io/NSIPremiere/reseau/#cours){target=_blank}.


## Activités 


{{ titre_activite("Adresse IP, masque",[],0) }}

!!! note
    Deux machines ne peuvent communiquer que si elles sont sur le même réseau, c'est à dire que leurs adresses {{sc("ip")}} démarre par une partie commune. La longueur de cette partie commune est définie par le **masque de sous réseau**. Pour la connaître, on écrit le masque de sous réseau en binaire. Le nombre de 1 en début de masque donne la longueur de la partie commune dans les adresses IP. Par exemple  le masque `255.255.254.0` donne en écriture binaire `11111111.11111111.111111110.00000000`. La partie commune doit donc être de 23 bits car cette écriture débute par 23 fois le chiffre `1`. Un masque de 23 bits peut se noter de façon plus concise `/23` (notation {{sc("cidr")}}). Pour savoir si deux machines de ce réseau peuvent communiquer on écrit leurs adresses IP en binaire et on regarde si les 23 premiers bits sont identiques ou non.

1. Lancer [Filius](https://www.lernsoftware-filius.de/), un outil de simulation de réseaux, et crée un simple réseau constitué de deux ordinateurs. Dans chacun des cas suivants, prévoir si les deux ordinateurs peuvent communiquer et le vérifier à l'aide d'une commande `ping`
    
    | IP ordinateur 1 | Masque Ordinateur 1 | IP ordinateur 2 | Masque ordinateur 2|
    |-----------------|---------------------|-----------------|--------------------|
    | 203.147.154.100 | 255.255.255.192     | 203.147.154.119 |  255.255.255.192   |
    | 203.147.154.100 | 255.255.255.192     | 203.147.154.129 |  255.255.255.192   |
    | 172.19.247.15   | 255.255.240.0       | 172.19.230.150  |  255.255.240.0     |
    | 172.19.247.15   | 255.255.240.0       | 172.19.248.118  |  255.255.240.0     | 

    !!! note
        l'adresse du réseau s'obtient en réalisant un *et* logique entre l'adresse IP d'un ordinateur du réseau et le masque de sous réseau.

{{ titre_activite("Protocole RIP",[]) }}

{{ titre_activite("Protocole OSPF",[]) }}


## Cours

{{ aff_cours(num) }}


## Exercices

{{ exo("....",[],0) }}

