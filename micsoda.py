import random
#eljárás visszatérés nélküli függvény, olyan függvény melynek nincsen visszatérési értéke

def pozitivSzamokAtlaga(lista):
    db=0
    osszeg=0
    for elem in lista:
        if(elem>0):
            db+=1
            osszeg+=elem
    atlag=osszeg/db
    return atlag

def listaAtlaga(lista):
    osszeg=0
    for elem in lista:
        osszeg+=elem
    atlag=osszeg/len(lista)
    return atlag

def maximumIndex(lista):
    maxi=0
    for i in range(len(lista)):
        if(lista[i]>(maxi)):
            maxi=lista[i]
    return maxi

def szamolas(lista):
    minimum=0
    maximum=0
    for i in range(len(lista)):
        if lista[i]>maximum:
            maximum=lista[i]
        if lista[i]<minimum:
            minimum=lista[i]
        terjedelem=maximum-minimum
    return terjedelem
def veletlenlista(n):
    n=13
    lista=[]
    for i in range(n):
        negative=random.randint(0,1)
        vszam=random.randint(2,19)*50
        if negative==0:
            lista.append(-1*vszam)
        else:
            lista.append(vszam)
   # print(lista)
    return lista
def negativraVegzodo(barmilyenlista):
    db=0
    for i in range(0,len(barmilyenlista),1):
        if(barmilyenlista[i]%100==0):
            db+=1


def main():
    lista1=veletlenlista(13)
    print(lista1)
    lista2=veletlenlista(5)
    print(lista2)

    print("00-ra végződő lista1", negativraVegzodo(lista1))
    print("00-ra végződő:", negativraVegzodo(lista2))

    listaAtlaga(lista1)
    print("Az első lista átlaga: ",listaAtlaga)
    print("A második lista átlaga: ", listaAtlaga(lista2))

    print("Az első lista pozitív számainak átlaga:", pozitivSzamokAtlaga(lista1))
    print("A második lista pozitív számainak átlaga:", pozitivSzamokAtlaga(lista2))
    maxlista1=maximumIndex(lista1)
    print("Első legnagyobb elem helye:", maxlista1) 

    print("A lista terjedelme: ",szamolas )
main()

#adjuk meg, hány darab negatív, 00-ra végződő szám van!
#Írjon függvényt, ami visszaadja a listánk terjedelmét. Terjedelem=Maximum-minimum
