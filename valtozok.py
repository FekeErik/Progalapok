nev="Feke Teréz"
osztaly="10.b"
datum="Mai nap"

print(nev,osztaly,datum,sep="\n")

#operátor

#konkatenálás
osszefuzes=nev+"bármi"+osztaly
print(osszefuzes)

#többszörözés

soknev=nev * 5
print(soknev)

"Typusok"
"- szöveg - string - str"
"(karakter)"
"-szam -egesz(int), lebegopont(float)"
"-logikai -true -false"

aEgesz=123
bTort=34.23
szSzam="12"
logikai=True

print("a Egész:", aEgesz)
print("b tört=", bTort)
print("sz Szam:", szSzam)
print("logikai:", logikai)

#egész operátorok
print("a + 2 =:", aEgesz + 2)
print("a - 2 =:", aEgesz - 2)
print("a * 2 =:", aEgesz * 2)
print("a / 2 =:", aEgesz / 2)

#Div - egészrész, Mod - modulus(maradék)

print("A div 8", aEgesz//8)
print("a mod 8", aEgesz % 8)

print(int(szSzam+aEgesz))
print(szSzam+str(aEgesz))

print(str(aEgesz)+szSzam)
print(aEgesz+int(szSzam))