

def vaneKetjegyuListaban(lista):
    i=0
    while(i<len(lista) and (lista[i]>=10 and lista[i]<99)):
        i+=1
    vane=i<len(lista)
    return vane

def main():
    szamok=[2,5,6,3,7,1,9,1,2]
    print(szamok)
    #van-e benne kétjegyű szám?
    vaneKetjegyu=vaneKetjegyuListaban(szamok)
    print(vaneKetjegyu)
    main()