sec=int(input("adja meg a számot"))

óra=sec%3600
perc=sec%60
másodperc=sec

if(sec%3600==0):
    óra+=1
elif(sec%60==0):
    perc+=1
else:
    sec+=sec

print(f"{óra} óra, {perc} perc, és {másodperc} másodpercre lehet osztani")