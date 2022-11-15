# DEBUT

import os

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
        else:
            i, j = int(input("choisir la ligne de la case souhaité : ")), int(input("choisir la colone de la case souhaité : "))
            if joueur == True:
                if tabmorpion[i][j] == 2:
                    tabmorpion[i][j] = 1
                    joueur = not joueur
                else : 
                    print("case déja utilisé ou incorrecte")
                    print('rejouer')
            else:
                if tabmorpion[i][j] == 2:
                    tabmorpion[i][j] = 0
                    joueur = not joueur
                else : 
                    print("case déja utilisé ou incorrecte")
                    print('rejouer')
            displaytab(tabmorpion)
        

print('morpion()')    