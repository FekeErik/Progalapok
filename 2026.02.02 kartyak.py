import random

def kartyaGeneralas():
    lista=[]
    for i in range(1,14,1):
        lista.append("T"+str(i))
        lista.append("P"+str(i))
        lista.append("K"+str(i))
        lista.append("S"+str(i))
    return lista

def keveres(pakli):
    sv=pakli[0]
    pakli[0]=pakli[1]
    pakli[1]=sv

def main():
    for i in range(10):
        a = random.randint(0,len(pakli)-1)
        b=random.randint(0,51)
        sv=pakli[a]
        pakli=kartyaGeneralas()
        #print(pakli)
        keveres(pakli)
        print(pakli)


main()