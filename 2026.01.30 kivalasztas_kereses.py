import random
def szamBekeres():
    szam=int(input("Adjon meg egy számot"))
    while not szam>=10 and szam<=20:
        print("Elrontottad")
        szam=int(input("Adjon meg egy ssámot 10,20 között"))
    return szam

def listaFeltoltes():
    lista=[]
    for i in range(n):
        szam=random.randint(10,99)

def main():
    db=szamBekeres()
    szamokLista=listaFeltoltes(db)
main()