#! /usr/bin/python3
import tkinter as tk
import tkinter.font as tkfont
from random import choice, randint

# Paramètres du jeu
NB_BATONS = 20
MAX_COUP = 3

# Paramètres d'affichage
W_WIDTH = 850
W_HEIGHT = 380
W_BGCOLOR = "blue"
B_BGCOLOR = "#666666"
W_TITLE = "Jeu des bâtonnets"
B_COLOR = "yellow"
B_WIDTH = 200
BG_CHOIX="#555555"
FG_CHOIX="yellow"
REPERE =  chr(0x2B24)
REPERE_COLOR= "orange"

# Placements des boutons
B_TEXT =[f"Retirer {i} bâtonnets" if i>1 else "Retirer 1 bâtonnet" for i in range(1,4)]
B_REMOVE_X=[70+250*i for i in range(3)]
B_REMOVE_Y = [250]*3
MB_X = 340
MB_Y = 10

# Apparence et position des batonnets 
BAT_OX = 30
BAT_OY = 60
BAT_W = 20
BAT_H = 160
BAT_COLOR = "#FFFFFF"
NOBAT_COLOR = "navy"
BAT_BORDER_COLOR = "brown"
BAT_BORDER_WIDTH = 3
NOBAT_BORDER_COLOR="#555555"

# Type de joueurs
TYPE_JOUEUR = ["Humain","IA Apprenante","IA Aléatoire","IA Experte"]

class Jeu:

    class Bouton:

        def __init__(self,fenetre,text,command,posx,posy):
            self.bouton=tk.Button(fenetre,text=text,command=command,bg=B_BGCOLOR,fg=B_COLOR,border=0)
            self.posx=posx
            self.posy=posy
            self.bouton.place(x=posx,y=posy,width=B_WIDTH)

    def __init__(self):
        self.fenetre=tk.Tk()
        self.canvas = tk.Canvas(master=self.fenetre,width=W_WIDTH,height=W_HEIGHT,bg=W_BGCOLOR)
        self.j1 = tk.StringVar(self.fenetre,"Humain")
        self.j2 = tk.StringVar(self.fenetre,"Humain")
        self.remove1=Jeu.Bouton(self.fenetre,B_TEXT[0],lambda : self.enlever(1),B_REMOVE_X[0],B_REMOVE_Y[0])
        self.remove2=Jeu.Bouton(self.fenetre,B_TEXT[1],lambda : self.enlever(2),B_REMOVE_X[1],B_REMOVE_Y[1])
        self.remove3=Jeu.Bouton(self.fenetre,B_TEXT[2],lambda : self.enlever(3),B_REMOVE_X[2],B_REMOVE_Y[2]) 
        self.quitter=Jeu.Bouton(self.fenetre,"Quitter",self.quitter,570,300)
        self.montrer_ia=Jeu.Bouton(self.fenetre,"Montrer IA",self.m_ia,70,300)
        self.cacher_ia=Jeu.Bouton(self.fenetre,"Cacher IA",self.c_ia,320,300)
        self.mainb=Jeu.Bouton(self.fenetre,"Commencer une partie",self.start,MB_X,MB_Y)
        self.canvas.create_text(80,20,text="Joueur 1 :",font=tkfont.Font(family='Helvetica',size=15, weight='bold'),fill="yellow",width=100)
        self.canvas.create_text(650,20,text="Joueur 2 :",font=tkfont.Font(family='Helvetica',size=15, weight='bold'),fill="yellow",width=100)
        self.choix_j1 = tk.OptionMenu(self.fenetre, self.j1, *TYPE_JOUEUR)
        self.choix_j2 = tk.OptionMenu(self.fenetre, self.j2, *TYPE_JOUEUR)
        self.nb_batons = NB_BATONS
        self.joueur_courant=randint(1,2)
        self.repere_joueur = tk.Label(self.fenetre,text=REPERE,fg=REPERE_COLOR,bg=W_BGCOLOR,font=("Arial",12,"bold"))
        self.message = tk.Label(self.fenetre,text="",fg="red",bg=W_BGCOLOR,font=("Arial",12,"bold"))
        self.vue_ia = tk.Label(self.fenetre,text="",fg="orange",bg=W_BGCOLOR,font=("Mono",10,"bold"))
        self.ia = {i:list(range(1,min(i,4))) for i in range(1,NB_BATONS+1)}
        self.voir_ia=False
        self.lpia1=None
        self.lpia2=None
        self.affiche()
    
    def enlever(self,nb):
        old_joueur = self.joueur_courant
        play=False
        if self.joueur_courant==1 and self.j1.get()=="Humain":
            self.joueur_courant=2 
            self.nb_batons-=nb
            play=True
        elif self.joueur_courant==2 and self.j2.get()=="Humain":
            self.joueur_courant=1
            self.nb_batons-=nb
            play=True
        if play:
            if self.nb_batons==1:
                self.message.configure(text=f"Joueur {self.joueur_courant} a perdu !")
            else:
                sbat ="bâtonnets"
                if nb==1: sbat=sbat[:-1]
                self.message.configure(text=f"Joueur {old_joueur} a enlevé {nb} {sbat} !")
            self.affiche()
        self.partie()

    def m_ia(self):
        self.voir_ia=True
        self.affiche()
    
    def c_ia(self):
        self.voir_ia=False
        self.affiche()
    

    def joue_coup(self,nb):
        old_joueur = self.joueur_courant
        play=False
        if self.joueur_courant==1:
            self.joueur_courant=2 
            self.nb_batons-=nb
            play=True
        elif self.joueur_courant==2:
            self.joueur_courant=1
            self.nb_batons-=nb
            play=True
        if play:
            if self.nb_batons==1:
                self.message.configure(text=f"Joueur {self.joueur_courant} a perdu !")
            else:
                sbat ="bâtonnets"
                if nb==1: sbat=sbat[:-1]
                self.message.configure(text=f"Joueur {old_joueur} a enlevé {nb} {sbat} !")
            self.affiche()
        self.partie()


    def affiche(self):
        self.choix_j1.config(bg=BG_CHOIX,fg=FG_CHOIX,borderwidth=0)
        self.choix_j1.place(x=140,y=5)
        self.choix_j2.config(bg=BG_CHOIX,fg=FG_CHOIX,borderwidth=0)
        self.choix_j2.place(x=710,y=5)
        self.fenetre.title(W_TITLE)
        if self.joueur_courant==1:
            self.repere_joueur.place(x=30,y=15,anchor=tk.E)
        else:
            self.repere_joueur.place(x=600,y=15,anchor=tk.E)
        if self.message=="":
            self.message.configure(fg=W_BGCOLOR)
        else:
            self.message.configure(fg="Orange")
        self.message.place(x=420,y=340,anchor=tk.N)
        self.vue_ia.configure(text=self.textia())
        self.affiche_ia()
        self.affiche_batons()
        self.canvas.update()
    
    def affiche_ia(self):
        if self.voir_ia:
            self.vue_ia.configure(fg="orange")
            self.vue_ia.place(x=BAT_OX-5,y=BAT_OY+BAT_H+5)
        else:
            self.vue_ia.configure(fg=W_BGCOLOR)

    def textia(self):
        tia = ""
        for k in self.ia:
            for p in range(1,4):
                if p in self.ia[k]:
                    tia+=str(p)
                else:
                    tia+="."
            tia+="  "
        return tia
            
    def affiche_batons(self):
        for i in range(NB_BATONS):
            if i<self.nb_batons:
                ccolor = BAT_COLOR
                bcolor = BAT_BORDER_COLOR
            else:
                ccolor = NOBAT_COLOR
                bcolor = NOBAT_BORDER_COLOR
            self.canvas.create_rectangle(BAT_OX+i*40,BAT_OY,BAT_OX+BAT_W+i*40,BAT_OY+BAT_H,fill=ccolor,width=BAT_BORDER_WIDTH,outline=bcolor)
            self.canvas.create_text(40+i*40,BAT_OY+BAT_H//2,text=str(i+1),font=tkfont.Font(family='Helvetica',size=12, weight='bold'))
        self.canvas.pack()

    def partie(self):
        if self.nb_batons>1:
            if (self.joueur_courant==1 and self.j1.get()=="IA Aléatoire") or  (self.joueur_courant==2 and self.j2.get()=="IA Aléatoire"):
                retire=randint(1,min(3,self.nb_batons-1))
                self.joue_coup(retire)
            if (self.joueur_courant==1 and self.j1.get()=="IA Experte") or  (self.joueur_courant==2 and self.j2.get()=="IA Experte"):
                if self.nb_batons%4==1:
                    retire=randint(1,min(3,self.nb_batons-1))
                else:
                    retire=(self.nb_batons%4-1)%4
                self.joue_coup(retire)
            if (self.joueur_courant==1 and self.j1.get()=="IA Apprenante") or  (self.joueur_courant==2 and self.j2.get()=="IA Apprenante"):
                if self.ia[self.nb_batons]!=[]:
                    retire=choice(self.ia[self.nb_batons])
                    if self.joueur_courant==1:
                        self.lpia1=self.nb_batons,retire
                    else:
                        self.lpia2=self.nb_batons,retire
                else:
                    retire=randint(1,min(3,self.nb_batons-1))
                self.joue_coup(retire)
        else:
            self.message.configure(text=f"Joueur {self.joueur_courant} a perdu !")
            if (self.joueur_courant==1 and self.j1.get()=="IA Apprenante") or  (self.joueur_courant==2 and self.j2.get()=="IA Apprenante"):
                if self.joueur_courant==1 and self.lpia1!=None:
                    self.ia[self.lpia1[0]].remove(self.lpia1[1])
                if self.joueur_courant==2 and self.lpia2!=None:
                    self.ia[self.lpia2[0]].remove(self.lpia2[1])
                self.affiche()

    def start(self):
        self.nb_batons=NB_BATONS
        self.message.configure(text="",fg=W_BGCOLOR)
        self.lpia1=None
        self.lpia2=None
        self.affiche()
        self.partie()
        self.loop()
    
    def loop(self):
        self.fenetre.mainloop()
    
    def quitter(self):
        self.fenetre.destroy()


nim = Jeu()
nim.start()


