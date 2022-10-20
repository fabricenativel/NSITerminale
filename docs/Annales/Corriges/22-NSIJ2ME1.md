{% set repere_sujet = "22-NSIJ2ME1" %}

{{ corrige_sujetbac(repere_sujet) }}


{{ corrige_exobac(repere_sujet,1) }}

1.  a. La taille de cet arbre est 8 (on utilise la définition donnée dans l'énoncé : "*la taille d’un arbre est le nombre de nœuds qu’il contient*)
    
    b.  La hauteur de cet arbre est 4 (on utilise la définition  donnée dans l'énoncé : *Sa hauteur est le nombre de nœuds du plus long chemin qui joint le nœud racine à l’une des feuilles*)
    
    !!! warning "Attention"
        D'autres auteurs donnent une définition différente de la hauteur dans laquelle la hauteur de l'arbre vide est $-1$.

    c.
    ```mermaid
    graph TD
    N21(("21")) --> N18(("18"))
    N21 --> N27(("27"))
    N18 --> V1[" "]
    N18 --> N20(("20"))
    style V1 fill:#FFFFFF, stroke:#FFFFFF
    linkStyle 2 stroke:#FFFFFF,stroke-width:0px
    ```

    d. Pour tout noeud de cet arbre, les valeurs figurant dans le sous arbre gauche sont inférieures à la valeur du noeud et celles du sous arbre droit son supérieures. C'est donc bien un arbre binaire de recherche.

    c. On a indiqué en rouge le chemin suivi pour insérer 17
    ```mermaid
    graph TD
    N15(("15")) --> N13(("13"))
    N15 --> N21(("21"))
    N13 --> N11(("11"))
    N13 --> N14(("14"))
    N21 --> N18(("18"))
    N21 --> N27(("27"))
    N18 --> N17(("17"))
    N18 --> N20(("20"))
    style N17 fill:#AA2222,stroke:#333
    linkStyle 1,4,6 stroke:#FF0000,stroke-width:2px
    ```

2.  a. C'est l'instruction **(C)** 

    b.  
    ```python
        return Noeud(ins(v,abr.gauche),abr.valeur,abr.droit)
    ```

    c. Chaque noeud (même lorsque ses fils sont `None`) génère deux appels récursif (un pour le fils droit et un pour le fils gauche). Chaque arête de l'arbre suivant représente donc un appel récursif :
    ```mermaid
    graph TD
    N15(("15")) --> N13(("13"))
    N15 --> N21(("21"))
    N13 --> N11(("11"))
    N13 --> N14(("14"))
    N21 --> N18(("18"))
    N18 --> V5["None"]
    N21 --> N27(("27"))
    N18 --> N20(("20"))
    N11 --> V1["None"]
    N11 --> V2["None"]
    N14 --> V3["None"]
    N14 --> V4["None"]
    N27 --> V6["None"]
    N27 --> V7["None"]
    N20 --> V8["None"]
    N20 --> V9["None"]
    style V5 V6 fill:#DDDDDD,stroke:#000000
    ```
    L'instruction `nb_sup(16,abr)` va donc générer un total de 17 appels à `nb_sup` (l'appel initial plus 16 appels récursifs).

    d. En utilisant la propriété des arbres binaires de recherche (rappelée à la question **1.d**), on sait qu'il suffit de chercher dans le sous arbre droit lorsque `abr.valeur<v`  puisque le sous arbre gauche contient des valeurs inférieures à `abr.valeur`.

    ```python
    def nb_sup(v, abr):
        if abr is None:
            return 0
        else:
            if abr.valeur >= v:
                return 1+nb_sup(v, abr.gauche)+nb_sup(v, abr.droit)
            return nb_sup(v, abr.droit)
    ```


{{ corrige_exobac(repere_sujet,2) }}

1.  a.
    Premiers parcours :
    <table><tr>
    <td>
    <div class="box">
    &#9475; <span class="rouge">4</span> &#9475;<br>
    &#9475; <span class="rouge"><del>9</del></span> &#9475;<br>
    &#9475; <span class="rouge">8</span> &#9475;<br>
    &#9475; 7 &#9475;<br>
    &#9475; 4 &#9475;<br>
    &#9475; 2 &#9475;<br>
    &#9495;&#9473;&#9473;&#9473;&#9499;
    </div>
    </td>
    <td>
    <div class="box">
    &#9475;   &nbsp; &#9475;<br>
    &#9475; 4 &#9475;<br>
    &#9475; <span class="rouge">8</span> &#9475;<br>
    &#9475; <span class="rouge"><del>7</del></span> &#9475;<br>
    &#9475; <span class="rouge">4</span> &#9475;<br>
    &#9475; 2 &#9475;<br>
    &#9495;&#9473;&#9473;&#9473;&#9499;
    </div>
    </td>
    <td>
    <div class="box">
    &#9475;   &nbsp; &#9475;<br>
    &#9475;   &nbsp; &#9475;<br>
    &#9475; 4 &#9475;<br>
    &#9475; 8 &#9475;<br>
    &#9475; 4 &#9475;<br>
    &#9475; 2 &#9475;<br>
    &#9495;&#9473;&#9473;&#9473;&#9499;
    </div>
    </td>
    </tr></table>
    Second parcours :
    <table><tr>
    <td>
    <div class="box">
    &#9475;   &nbsp; &#9475;<br>
    &#9475;   &nbsp; &#9475;<br>
    &#9475; <span class="rouge">4</span> &#9475;<br>
    &#9475; <span class="rouge"><del>8</del></span> &#9475;<br>
    &#9475; <span class="rouge">4</span> &#9475;<br>
    &#9475; 2 &#9475;<br>
    &#9495;&#9473;&#9473;&#9473;&#9499;
    </div>
    </td>
    <td>
    <div class="box">
    &#9475;   &nbsp; &#9475;<br>
    &#9475;   &nbsp; &#9475;<br>
    &#9475;   &nbsp; &#9475;<br>
    &#9475; 4 &#9475;<br>
    &#9475; 4 &#9475;<br>
    &#9475; 2 &#9475;<br>
    &#9495;&#9473;&#9473;&#9473;&#9499;
    </div>
    </td>
    </tr></table>
    Troisième parcours :
    <table><tr>
    <td>
    <div class="box">
    &#9475;   &nbsp; &#9475;<br>
    &#9475;   &nbsp; &#9475;<br>
    &#9475; <span class="rouge">4</span> &#9475;<br>
    &#9475; <span class="rouge"><del>4</del></span> &#9475;<br>
    &#9475; <span class="rouge">2</span> &#9475;<br>
    &#9495;&#9473;&#9473;&#9473;&#9499;
    </div>
    </td>
    <td>
    <div class="box">
    &#9475;   &nbsp; &#9475;<br>
    &#9475;   &nbsp; &#9475;<br>
    &#9475;   &nbsp; &#9475;<br>
    &#9475; 4 &#9475;<br>
    &#9475; 2 &#9475;<br>
    &#9495;&#9473;&#9473;&#9473;&#9499;
    </div>
    </td>
    </tr></table>
    Cette pile est donc gagnante.

    b. La pile **B** est gagnante, en effet :
    <table><tr>
    <td>
    <div class="box">
    &#9475; <span class="rouge">4</span> &#9475;<br>
    &#9475; <span class="rouge"><del>5</del></span> &#9475;<br>
    &#9475; <span class="rouge">4</span> &#9475;<br>
    &#9475; 9 &#9475;<br>
    &#9475; 2 &#9475;<br>
    &#9475; 0 &#9475;<br>
    &#9495;&#9473;&#9473;&#9473;&#9499;
    </div>
    </td>
    <td>
    <div class="box">
    &#9475;   &nbsp; &#9475;<br>
    &#9475; 4 &#9475;<br>
    &#9475; <span class="rouge">4</span> &#9475;<br>
    &#9475; <span class="rouge"><del>9</del></span> &#9475;<br>
    &#9475; <span class="rouge">2</span> &#9475;<br>
    &#9475; 0 &#9475;<br>
    &#9495;&#9473;&#9473;&#9473;&#9499;
    </div>
    </td>
    <td>
    <div class="box">
    &#9475;   &nbsp; &#9475;<br>
    &#9475;   &nbsp; &#9475;<br>
    &#9475; 4 &#9475;<br>
    &#9475; 4 &#9475;<br>
    &#9475; 2 &#9475;<br>
    &#9475; 0 &#9475;<br>
    &#9495;&#9473;&#9473;&#9473;&#9499;
    </div>
    </td>
    </tr></table>
    Second parcours :
    <table><tr>
    <td>
    <div class="box">
    &#9475;   &nbsp; &#9475;<br>
    &#9475;   &nbsp; &#9475;<br>
    &#9475; <span class="rouge">4</span> &#9475;<br>
    &#9475; <span class="rouge"><del>4</del></span> &#9475;<br>
    &#9475; <span class="rouge">2</span> &#9475;<br>
    &#9475; 0 &#9475;<br>
    &#9495;&#9473;&#9473;&#9473;&#9499;
    </div>
    </td>
    <td>
    <div class="box">
    &#9475;   &nbsp; &#9475;<br>
    &#9475;   &nbsp; &#9475;<br>
    &#9475;   &nbsp; &#9475;<br>
    &#9475; 4 &#9475;<br>
    &#9475; 2 &#9475;<br>
    &#9475; 0 &#9475;<br>
    &#9495;&#9473;&#9473;&#9473;&#9499;
    </div>
    </td>
    </tr></table>
    Troisième parcours :
    <table><tr>
    <td>
    <div class="box">
    &#9475;   &nbsp; &#9475;<br>
    &#9475;   &nbsp; &#9475;<br>
    &#9475; <span class="rouge">4</span> &#9475;<br>
    &#9475; <span class="rouge"><del>2</del></span> &#9475;<br>
    &#9475; <span class="rouge">0</span> &#9475;<br>
    &#9495;&#9473;&#9473;&#9473;&#9499;
    </div>
    </td>
    <td>
    <div class="box">
    &#9475;   &nbsp; &#9475;<br>
    &#9475;   &nbsp; &#9475;<br>
    &#9475;   &nbsp; &#9475;<br>
    &#9475; 4 &#9475;<br>
    &#9475; 0 &#9475;<br>
    &#9495;&#9473;&#9473;&#9473;&#9499;
    </div>
    </td>
    </tr></table>

2. Code complété :
```python
def reduire_triplet_au_sommet(p):
    a = depiler(p)
    b = depiler(p)
    c = sommet(p)
    if a % 2 != c%2 :
        empiler(p, b)
    empiler(p, a)
```

    !!! Attention
        La méthode `sommet` renvoie le sommet *sans le dépiler*, suivant le résultat du test de parité on rempile ou non l'élément central du triplet.

3.  a. La taille minimal d'une pile réductible est 3.

    b. 
```python
    def parcourir_pile_en_reduisant(p):
        q = creer_pile_vide()
        while taille(p) >= 3:
            reduire_triplet_au_sommet(p)
            e = depiler(p)
            empiler(q, e)
        while not est_vide(q):
            e = depiler(q)
            empiler(p,e)
        return p
```

4.  Code complété :

```python linenums="1"
def jouer(p):
    q = parcourir_pile_en_reduisant(p)
    if taille(q)==taille(p) :
        return p
    else:
        return jouer(q)
``` 

!!! Bug
    La structure de données pile de l'énoncé est *mutable*. En effet, par exemple `depiler(p)` retire le sommet de `p` et donc modifie `p`. Par conséquent, `parcourir_pile_en_reduisant` modifie la pile passée en paramètre (en dépit du `return` qui figure dans cette fonction et laisse penser qu'on renvoie une nouvelle pile). Bien que la correction proposée ci-dessus est probablement la réponse attendue, elle ne fonctionne pas car `p` et `q` sont le même objet et le test ligne 3 est vérifié. 
    Le site [écrit {{sc("nsi")}}](https://e-nsi.gitlab.io/ecrit/Struct/22-ME2-ex2/) propose une correction de Nicolas Reveret avec modification de l'énoncé afin d'éviter ce bug.

{{ corrige_exobac(repere_sujet,3) }}

1.  a. L'adresse du réseau est `192.168.1.0` pour l'obtenir il suffit de faire un *et* logique bit à bit entre l'adresse de la machine `192.168.1.0` et le masque du réseau qui est ici `255.255.255.0` (soir `\24\ en notation {{sc("cidr")}})

2.  

{{ corrige_exobac(repere_sujet,4) }}

{{ corrige_exobac(repere_sujet,5) }}
