# DEBUT

import os
from tkinter import *

tabmorpion = [
    ['□',"1","2","3"],
    ['1',2,2,2],
    ['2',2,2,2],
    ['3',2,2,2]
]

tabresultat = [
    ['□',"1","2","3"],
    ['1',' ',' ',' '],
    ['2',' ',' ',' '],
    ['3',' ',' ',' ']
]

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def displaytab(tab):
    cls()
    for x in range(len(tab)):
        for y in range(len(tab)):
            if tab[x][y] == 2:
                tabresultat[x][y] = ' '
            elif tab[x][y] == 1:
                tabresultat[x][y] = '⬤'
            elif tab[x][y] == 0:
                tabresultat[x][y] = '✚'
    for i in tabresultat:
        print(i)

def graphique():
    root = Tk()
    root.title('Morpion')
    root.grid()
    qb1 = Button(root, text=tabresultat[1][1],padx = 50,pady = 50)
    qb2 = Button(root, text=tabresultat[1][2],padx = 50,pady = 50)
    qb3 = Button(root, text=tabresultat[1][3],padx = 50,pady = 50)
    qb4 = Button(root, text=tabresultat[2][1],padx = 50,pady = 50)
    qb5 = Button(root, text=tabresultat[2][2],padx = 50,pady = 50)
    qb6 = Button(root, text=tabresultat[2][3],padx = 50,pady = 50)
    qb7 = Button(root, text=tabresultat[3][1],padx = 50,pady = 50)
    qb8 = Button(root, text=tabresultat[3][2],padx = 50,pady = 50)
    qb9 = Button(root, text=tabresultat[3][3],padx = 50,pady = 50)
    qb1.grid(row=0, column=0)
    qb2.grid(row=0, column=1)
    qb3.grid(row=0, column=2)
    qb4.grid(row=1, column=0)
    qb5.grid(row=1, column=1)
    qb6.grid(row=1, column=2)
    qb7.grid(row=2, column=0)
    qb8.grid(row=2, column=1)
    qb9.grid(row=2, column=2)
    root.mainloop()

def morpion():
    print("""
    ------------------- JEU DU MORPION -----------------------
    - ceci est un jeu du morpion
    - il ce joue a deux ou a plus par equipe
    - il suffit de lancer la commande morpion
    - amuser vous bien
    ----------------------------------------------------------- 
    """)
    displaytab(tabmorpion)
    joueur = True
    while True:
        # victoire joueur1
        if (tabmorpion[1][1], tabmorpion[1][2], tabmorpion[1][3]) == (1,1,1) or (tabmorpion[2][1], tabmorpion[2][2], tabmorpion[2][3]) == (1,1,1) or (tabmorpion[3][1], tabmorpion[3][2], tabmorpion[3][3]) == (1,1,1):
            print("joueur1 a gagné")
            return
        elif (tabmorpion[1][1], tabmorpion[2][1], tabmorpion[3][1]) == (1,1,1) or (tabmorpion[1][2], tabmorpion[2][2], tabmorpion[3][2]) == (1,1,1) or (tabmorpion[1][3], tabmorpion[2][3], tabmorpion[3][3]) == (1,1,1):
            print("joueur1 a gagné")
            return
        elif (tabmorpion[1][3], tabmorpion[2][2], tabmorpion[3][1]) == (1,1,1) or (tabmorpion[1][1], tabmorpion[2][2], tabmorpion[3][3]) == (1,1,1):
            print("joueur1 a gagné")
            return
        # victoire joueur2
        elif (tabmorpion[1][1], tabmorpion[1][2], tabmorpion[1][3]) == (0,0,0) or (tabmorpion[2][1], tabmorpion[2][2], tabmorpion[2][3]) == (0,0,0) or (tabmorpion[3][1], tabmorpion[3][2], tabmorpion[3][3]) == (0,0,0):
            print("joueur2 a gagné")
            return
        elif (tabmorpion[1][1], tabmorpion[2][1], tabmorpion[3][1]) == (0,0,0) or (tabmorpion[1][2], tabmorpion[2][2], tabmorpion[3][2]) == (0,0,0) or (tabmorpion[1][3], tabmorpion[2][3], tabmorpion[3][3]) == (0,0,0):
            print("joueur2 a gagné")
            return
        elif (tabmorpion[1][3], tabmorpion[2][2], tabmorpion[3][1]) == (0,0,0) or (tabmorpion[1][1], tabmorpion[2][2], tabmorpion[3][3]) == (0,0,0):
            print("joueur2 a gagné")
            return
        # egalité
        elif (tabmorpion[1][1],tabmorpion[1][2],tabmorpion[1][3],tabmorpion[2][1],tabmorpion[2][2],tabmorpion[2][3],tabmorpion[3][1],tabmorpion[3][2],tabmorpion[3][3]) != (2,2,2,2,2,2,2,2):
            print("égalite")
            return
        else:
            i, j = int(input("choisir la ligne de la case souhaité : ")), int(input("choisir la colone de la case souhaité : "))
            if 1 <= i <= 3 and 1 <= j <= 3: 
                if joueur == True:
                    if tabmorpion[i][j] == 2:
                        tabmorpion[i][j] = 1
                        joueur = not joueur
                    else : 
                        print("case déja utilisé")
                        print('rejouer')
                else:
                    if tabmorpion[i][j] == 2:
                        tabmorpion[i][j] = 0
                        joueur = not joueur
                    else : 
                        print("case déja utilisé")
                        print('rejouer')
            else :
                print("la case souhaité est incorrecte")
            displaytab(tabmorpion)
        

graphique()   