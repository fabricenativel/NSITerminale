{% set repere_sujet = "21-NSIJ2ME1" %}
{% set numero_exo = 4 %}

{{ correction_exobac(repere_sujet,numero_exo) }}


#### Partie A

1. Si chaque programme s'exécute à tour de rôle, après la première instruction de chaque programme les 3 ressources sont prises. Un interblocage se produit donc car chaque programme a besoin d'une ressource détenu par un autre pour continuer son exécution.

2. On inverse l'ordre des demandes dans le programme 3. Ainsi c'est la table traçante qui est demandé en premier, comme elle est détenue par le programme 1. Le programme 3 est bloqué. Mais le programme 2 peut continuer car il dispose de sa seconde ressource (l'imprimante). Donc il peut s'exécuter et libérer ses ressources ce qui permet au programme 3 et 1 de terminer aussi.

3.  Le processus p1 sera dans l'état bloqué, c'est donc la réponse b)

#### Partie B

1. C'est la commande `ps -ef` c'est donc la réponse b)

2. C'est l'identifiant 831

3. C'est l'identifiant 6211

