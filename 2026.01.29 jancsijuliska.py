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

def vaneKetszamKozott(a,b,lista):
    index=0
    while(index<len(lista) and lista[index]<a and lista[index]<b) :
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
    vaneJuliska=vaneSzamnalNagyobb(8.5, juliska)
    if (vaneJuliska):
        print("Van Juliskánál 8,5-nél nagyobb")
    else:
        print("Nincs nála 8,5-nél nagyobb")

    vaneJuliskaKozott=vaneKetszamKozott(4.9,5.1,juliska)
    if vaneJuliska:
        print("Juliskának van 4,9 és 5,1 közötti értéke")
    else:
        print("Juliskának nincs  4,9 és 5,1 közötti értéke")

    
    vaneJancsiKozott=vaneKetszamKozott(4.9,5.1,jancsi)
    if vaneJancsiKozott:

        print("Jancsinak van 4,9 és 5,1 közötti értéke")
    else:
        print("Jancsinak nincs  4,9 és 5,1 közötti értéke")
main()