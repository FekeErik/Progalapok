"""
lista - dinamikus
    -tudunk bele új elemet rakni, ezzel nő az elemszáma.
    -tudunk belőle törölni, ezzel csökken az elemszáma
    -lekérhető bármelyik eleme
    -módosítható bármelyik elem
deklalárás:
lista_neve=[]
új elem hozzáadása
lista_neve.append(ujelem)
elem törlése:
lista_neve.remove(elem)
beégetett lista:
lista_neve[3,2,5,7,1]
lista hossza:
len(lista_neve)
"""

lista=["Blyat", "Nahui", "Pitchka", "Mudak", "Genghis khan"]
print(len(lista),lista[0],(lista-1))