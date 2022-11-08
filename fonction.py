def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mult(x,y):
    return x * y

def div(x,y):
    # je fais la division si le divisuer n'est pas egal a 0
    if y == 0:
        #renvoie erreur si il y a une divison par 0
        return "erreur division par 0 changer la deuxieme valeur" 
    return x / y

def mod(x,y):
    return x//y

def sal(salaireH,Hjo,JOans):
    #calcul salaire journalier
    x=mult(salaireH,Hjo) 
    #calcul salaire annuel
    y=mult(x,JOans) 
    #calcul salaire par seconde sur 1 ans
    z=div(y,(365*24*60*60)) 
    return z

def net(brut,fonction):
    #si fonctionnaire calcul salaire net avec 15% taxe
    if fonction == "publique":
        x = brut * (1-15/100) 
    #sinon calcul salaire net avec 23% taxe 
    else:
        x = brut * (1-23/100)  
    return x

def jeu():
    secret = 'z' 
    while secret != input('choisi lettre'):
        print('mauvaise lettre')
    print('bonne lettre')
    return 'bravo'
