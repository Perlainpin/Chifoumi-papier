def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mult(x,y):
    return x * y

def div(x,y):
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
    #calcul salaire net d'un fonctionnaire
    if fonction == "publique":
        x = brut * (1-15/100) 
    #calcul salaire net d'un employé
    else:
        x = brut * (1-23/100)  
    return x