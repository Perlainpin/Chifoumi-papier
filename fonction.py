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

tab = [0,1,2,0,4,5,6,0,8,9,10]

def index(list,val):
    x = 0
    char = ''
    for i in tab:
        if val == list[x]:
            if char != '':
                char += ', ' + str(x) 
            else:
                char += str(x)
        x += 1
    return char
        
def conca(char1,char2):
    strchar1 = str(char1)
    strchar2 = str(char2)
    return strchar1 + ', ' + strchar2

def msg(x):
    print(x)

userlist = {"alex":"123","des-vans":"456","kotob":"789"}

def login(user,password,list):
    for key , value in list.items():
        if key == user and value == password:
            print( "connexion bonne" )
            return
        print( "erreur connexion" )
        return


# definir un fonction qui recupere l'index du valeur x dans une liste tab
def indexp(tab,x):
    # innitialisation de i qui est l'index , de chaineresulta qui sea la liste d'index et de firstturn qui verifie la beauté de chaineresulta
    i=0
    charesult = ''
    firstturn = True
    # tant que i est pas plus grand que la longeur de tab
    while i < len(tab):
        # si la valeur de tab correspondant a l'index i est egal a x
        if tab[i] == x:
            # alors on surveille si c'est le premier index mis dans chaineresulta pour concatené sans avoir " x"  
            if firstturn == True:
                charesult += str[i]
                firstturn = False
            # sinon on concataine juste 
            else:
                charesult = conca(charesult,str[i])
        # on ajoute 1 a i pour decaler l'index
        i +=1
    # enfin on retourne chaineresult
    return charesult