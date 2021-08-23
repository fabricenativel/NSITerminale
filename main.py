def define_env(env):
    env.variables['transversal']=["histoire","projet","typesconstruits","python"]
    env.variables['projet'] = {"icone":":fontawesome-solid-lightbulb:","style":"projet"}
    env.variables['typesconstruits'] = {"icone":":fontawesome-solid-cubes:","style":"typesconstruits"}
    env.variables['python'] = {"icone":":fontawesome-brands-python:","style":"python"}
    env.variables['themes']={
        "histoire":"Histoire de l'informatique",
        "projet":"Projet",
        "sd":"Structures de données",
        "db":"Bases de données",
        "os":"Architectures matérielles, systèmes d'exploitation et réseaux",
        "algorithmique":"Algorithmique",
        "python":"Langages et programmation"
    }
    env.variables['icones'] = {
        "histoire":':fontawesome-solid-university:{title="'+env.variables['themes']['histoire']+'"}',
        "projet":':fontawesome-solid-lightbulb:{title="'+env.variables['themes']['projet']+'"}',
        "sd":':fontawesome-solid-project-diagram:{title="'+env.variables['themes']['sd']+'"}',
        "db":':fontawesome-solid-database:{title="'+env.variables['themes']['db']+'"}',
        "os":':fontawesome-solid-microchip:{title="'+env.variables['themes']['os']+'"}',
        "algorithmique":':fontawesome-solid-cogs:{title="'+env.variables['themes']['algorithmique']+'"}',
        "python":':fontawesome-brands-python:{title="'+env.variables['themes']['python']+'"}'
    }
    env.variables['icones_exo']={
        "dur": ":fontawesome-solid-bomb:{title='Exercice difficile'}",
        "rappel": ":fontawesome-solid-history:{title='Retour sur des notions antérieures'}",
        "recherche": ":fontawesome-solid-search:{title='Exercice de recherche'}",
        "capacite": ":fontawesome-solid-puzzle-piece:{title='Exercice testant une capacité du chapitre'}",
        "python": ":fontawesome-brands-python:{title='Exercice en lien avec la programmation en Python'}",
        "bac": ":fontawesome-solid-graduation-cap:{title='Exercice extrait du Bac'}",
        "maths": ":fontawesome-solid-infinity:{title='Exercice en lien avec les mathématiques'}"
    }
    env.variables['icones_act']={
        "rappel": ":fontawesome-solid-history:{title='Retour sur des notions antérieures'}",
        "recherche": ":fontawesome-solid-search:{title='Activité de recherche'}",
        "oral": ":fontawesome-solid-comments:{title='Activité oral'}",
        "papier": ":fontawesome-solid-edit:{title='Activité à réaliser sur feuille'}",
        "vscode": ":material-microsoft-visual-studio-code:{title='Activité utilisant VS Code'}",
        "video": ":fontawesome-solid-film:{title='Activité utilisant un support vidéo'}",
        "notebook": ":fontawesome-solid-book:{title='Activité utilisant un jupyter notebook'}",
        "python": ":fontawesome-brands-python:{title='Activité en lien avec la programmation en Python'}"
    }
    env.variables['devant_exo']=':black_small_square:'
    env.variables['devant_act']=':black_small_square:'
    env.variables['num_exo']=1
    env.variables['num_act']=1

    env.variables['progression']={
        0 : ["python","Révisions",2,"revisions.md"],
        1 : ["python","Récursivité",2,"recursivite.md"],
        2 : ["db","Bases de données et SQL",2,"sql.md"],
        3 : ["os","Processus",1,"processus.md"],
        4 : ["algorithmique","Diviser pour régner",1,"diviser.md"],
        5 : ["python","Notions de programmation orienté objet",2,"poo.md"],
        6 : ["sd","Structures de données linéaires",2,"sl.md"],
        7 : ["os","Système sur puce",1,"puces.md"],
        8 : ["sd","Arbres",2,"arbres.md"],
        9 : ["db","Schéma relationnel d'une base de données",2,"sgbd.md"],
        10: ["algorithmique","Algorithmes sur les arbres",2,"algoarbre.md"],
        11: ["sd","Graphes",2,"graphes.md"],
        12: ["os","Protocoles de routage",2,"routage.md"],
        13: ["algorithmique","Recherche textuelle",2,"texte.md"],
        14: ["python","Calculabilité, décidabilité",2,"calculabilite.md"],
        15: ["os","Sécurisation des communications",2,"cryptage.md"]
    }
    
    env.variables['nchap']=0
    env.variables['nelements']=0
    
    # Titres des items travaillés sur l'année
    @env.macro
    def sec_titre(theme,titre):
            icone = env.variables.icones[theme]
            return f"### {icone} &nbsp; {titre}"
    
    @env.macro
    def icone(theme):
        return env.variables.icones[theme]
    
    @env.macro
    def titre_chapitre(numero,titre,theme):
        # Position de l'ancre pour repérage dans la page
        titre_bis = env.variables['progression'][numero][1]
        ligne=f"# <span class='numchapitre'>C{numero}</span> {titre_bis} "
        ligne+=f"<span style='float:right;'>{env.variables.icones[theme]}</span>"
        return ligne
    
    @env.macro
    def titre_activite(titre,licones,numero=1):
        if numero==0:
            env.variables['num_act']=1
        ligne=f"### {env.variables['devant_act']}   Activité {env.variables['num_act']} "
        if titre!="":
            ligne+=f": *{titre}*"
        if licones!=[]:
            ligne+=f"<span style='float:right;'>"
            for icone in licones:
                ligne+=f"<span style='float:right;'>&thinsp; {env.variables['icones_act'][icone]}</span>"
            ligne+="</span>"
        env.variables['num_act']=env.variables['num_act']+1
        return ligne
    

    @env.macro
    def exo(titre,licones,numero=1):
        if numero==0:
            env.variables['num_exo']=1
        ligne=f"### {env.variables['devant_exo']}   Exercice {env.variables['num_exo']} "
        if titre!="":
            ligne+=f": *{titre}*"
        if licones!=[]:
            ligne+=f"<span style='float:right;'>"
            for icone in licones:
                ligne+=f"<span style='float:right;'>&thinsp; {env.variables['icones_exo'][icone]}</span>"
            ligne+="</span>"
        env.variables['num_exo']=env.variables['num_exo']+1
        return ligne
    
    @env.macro
    def liens(fichier,type=".pdf"):
        location="./pdf/"+fichier[0:2]+"/"
        return f"[:fontawesome-solid-download:]({location}{fichier}.pdf) [:fontawesome-regular-file:]({location}{fichier}.tex)"

    @env.macro
    def telecharger(description,fichier):
        liens =f"[{description} :material-download:](./{fichier})"
        liens+="{.md-button}"
        return "<span class='centre'>"+liens+"</span>"

    @env.macro
    def cours(fichier):
        ccours = '''
Vous pouvez télécharger une copie au format pdf du diaporama de synthèse de cours présenté en classe :

<span class='centre'>[Diaporama de cours :fontawesome-regular-file-pdf:](./pdf/'''+fichier+'''){.md-button}</span>
!!! warning "Attention"
    Ce diaporama ne vous donne que quelques points de repères lors de vos révisions. Il devrait être complété par la relecture attentive de vos **propres** notes de cours et par une révision approfondie des exercices.'''
        return ccours

    @env.macro
    def aff_cours(num):
        fichier=f'C{num}/C{num}-cours.pdf'
        return cours(fichier)

    @env.macro
    def sc(chaine):
        return f'<span style="font-variant:small-caps;">{chaine}</span>'

    @env.macro
    def chapitre(num,theme,titre,duree,lien):
        icone = env.variables["icones"][theme]
        return f"|{icone}|[C{num}- {titre}]({lien}) | {duree}\n"

    @env.macro
    def affiche_progression():
        ret='''
| |Titre        | Durée |
|-|-------------|-------|
        '''
        for k in env.variables.progression:
           ret+=chapitre(k,env.variables['progression'][k][0],env.variables['progression'][k][1],env.variables['progression'][k][2],env.variables['progression'][k][3])
        return ret
    
    @env.macro
    def genere_nav():
        ret='''```\n'''
        for k in env.variables.progression:
            da = env.variables['progression'][k]
            ret+=f'  - "C{k}-{da[1]}" : {da[3]}\n'
        return ret+'```\n'
    
    @env.macro
    def ok():
        return ":fontawesome-solid-check:{.vert title='Compatible'}"
    
    @env.macro
    def nok():
        return ":fontawesome-solid-times:{.rouge title='Non compatible'}"
    

    



    
