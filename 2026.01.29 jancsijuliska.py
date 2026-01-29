import random

def listaFeltolt(n):
    lista=[]
    for i in range(0,n,1):
        # lista.append(random.randint(200,900)/100)
        lista.append(round(random.random()*7+2,2)) #[0,1]
    return lista

def vaneSzamnalNagyobb(szam, lista):
    index=0
    while(index<len(lista) and lista[index] <=szam):
        index+=1
    vane=index<len(lista)
    return vane

def main():
    jancsi=[]
    juliska=[]
    #db = int(input())
    listaFeltolt(14)
    jancsi=listaFeltolt(14)
    juliska=listaFeltolt(14)
    print("Juliska: ", juliska)
    print("Jancsi", jancsi)
    vane=vaneSzamnalNagyobb(8,5)

main()