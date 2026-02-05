import random

def listaFeltoltes():
    lista=[]
    for i in range(0,17,1):
        valsz=random.randint(0,100)
        if valsz >=50:
            lista.append(random.randint(120,200))
        else:
            lista.append(random.randint(50,120))

    return lista
def listaAtlag(lista):
    osszeg=0
    for i in range(0,len(lista),1):
        osszeg+=lista[i]
    atlag=osszeg/len(lista)
    return atlag

def listaMaximuma(lista):
    maxi=lista[0]
    for i in range(1,len(lista),1):
        if(lista[i]>maxi):
            maxi=lista[i]
    return maxi

def listaMinimuma(lista):
    mini=lista[0]
    for i in range(1,len(lista),1):
        if(lista[i]<mini):
            mini=lista[i]
    return mini

def listaTerjedelme(lista):
    maximum=listaMaximuma(lista)
    minimum=listaMinimuma(lista)
    return maximum-minimum

def vaneMaxpontos(lista):
    n=200
    index=0
    while (index<(len(lista) and lista[index]!=200)):
        index+=1
    vane=index<len(lista)
    return vane

def dontobeJutottakDB(lista):
    db=0
    for i in range(0, len(lista), 1):
        if(lista[i]/200*100>= 70):
            db+=1
    return db
    
def ertek50Index(lista):
    i = 0
    while (i<len(lista) and lista[i]!=50):
        i+=1
    vane=i<len(lista)
    if vane:
        return i
    else:
        return -1

def main():
    pontok=listaFeltoltes()
    print(pontok)

    atlag=listaAtlag(pontok)
    print("Átlag: ", round(atlag,2))

    terjedelem=listaTerjedelme(pontok)
    print("terjedelem",terjedelem)
    print(terjedelem)

    vaneMaxpont = vaneMaxpontos(pontok)
    darab=dontobeJutottakDB(pontok)
    print(darab, "Tanuló jutott a döntőbe")

    index=ertek50Index(pontok)
    if index==-1:
        print("Nincs 50 pontos dolgozat a versenyen")
    else:
        print("A(z)", str(index), ". helyen van az 50 pontos dolgozat")
main()