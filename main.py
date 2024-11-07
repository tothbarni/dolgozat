import feladatok

print("1. feladat")
feladatok.feladat1()

print("2. feladat")
db = feladatok.feladat2()
print(f"A számok között {db}db 3-mal osztható szám van!")

print("3. feladat")
n_betu = feladatok.feladat3("Ez az én dumám", 4)

print("4. feladat")
nev:str = input("Adj meg egy nevet, vagy lépj ki '@'-karakterrel : ")
feladatok.feladat4(nev)

print("5. feladat")
tipp:str = input("Tipped: ")
feladatok.feladat5(tipp)