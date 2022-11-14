# DEBUT

tabmorpion = [
    ['□',"1","2","3"]
    ['A',0,0,0]
    ['B',0,0,0]
    ['C',0,0,0]
]

def displaytab(tab):
    for i in tab:
        print(i)

def morpion():
    displaytab(tabmorpion)
    while True:
        # victoire joueur1
        if (tabmorpion[1][1], tabmorpion[1][2], tabmorpion[1][3]) == (1,1,1) or (tabmorpion[2][1], tabmorpion[2][2], tabmorpion[2][3]) == (1,1,1) or (tabmorpion[3][1], tabmorpion[3][2], tabmorpion[3][3]) == (1,1,1):
            print("vous aver gagné")
            return
        elif (tabmorpion[1][1], tabmorpion[2][1], tabmorpion[3][1]) == (1,1,1) or (tabmorpion[1][2], tabmorpion[2][2], tabmorpion[3][2]) == (1,1,1) or (tabmorpion[1][3], tabmorpion[2][3], tabmorpion[3][3]) == (1,1,1):
            print("vous avez gagné")
            return
        elif (tabmorpion[1][3], tabmorpion[2][2], tabmorpion[3][1]) == (1,1,1) or (tabmorpion[1][1], tabmorpion[2][2], tabmorpion[3][3]) == (1,1,1):
            print("vous avez gagné")
            return
        # victoire joueur2
        elif (tabmorpion[1][1], tabmorpion[1][2], tabmorpion[1][3]) == (0,0,0) or (tabmorpion[2][1], tabmorpion[2][2], tabmorpion[2][3]) == (0,0,0) or (tabmorpion[3][1], tabmorpion[3][2], tabmorpion[3][3]) == (0,0,0):
            print("vous aver gagné")
            return
        elif (tabmorpion[1][1], tabmorpion[2][1], tabmorpion[3][1]) == (0,0,0) or (tabmorpion[1][2], tabmorpion[2][2], tabmorpion[3][2]) == (0,0,0) or (tabmorpion[1][3], tabmorpion[2][3], tabmorpion[3][3]) == (0,0,0):
            print("vous avez gagné")
            return
        elif (tabmorpion[1][3], tabmorpion[2][2], tabmorpion[3][1]) == (0,0,0) or (tabmorpion[1][1], tabmorpion[2][2], tabmorpion[3][3]) == (0,0,0):
            print("vous avez gagné")
            return
        else:
            
        