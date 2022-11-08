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
    x=mult(salaireH,Hjo)
    y=mult(x,JOans)
    z=div(y,31536000)
    return z

def net(brut,fonction):
    if fonction == "publique":
        x = brut * (1-15/100)
    else:
        x = brut * (1-23/100)
    return x