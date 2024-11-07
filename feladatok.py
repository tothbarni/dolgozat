import random
def feladat1():
    szam:int = int(input("Kérek egy páros számot : "))
    while (szam % 2 != 0):
        szam:int = int(input("Ez nem páros! PÁROS számot kérek! "))

def feladat2():
    db = 0
    for i in range(0, 13, 1):
        szam:int = int(random.random()* 141) + 10
        if (szam % 3 == 0):
            db += 1
    return db

def feladat3(szoveg:str, N:int):
    if (len(szoveg) < N):
        print(f"Nincs {N}. karakter!")
    else:
        karakter:str = (szoveg[N])
        n_betu:str = str(karakter.upper())
        print(f"A szöveg {N}. karaktere {karakter} - {str(n_betu) * 3}")

def feladat4(nev:str):
    nevek = []
    while (nev != "@"):
        nev:str = input("Adj meg egy nevet, vagy lépj ki '@'-karakterrel : ")
        nevek.append(nev)
    db:int = len(nevek)
    print(f"A felhasználó {db} nevet adott meg.")

def feladat5(tipp):
    felhasznalo_tippje = tipp.lower()
    gep_tipp = int(random.random() * 3) + 1
    if (gep_tipp == 1):
        gep_tipp = "kő"
    elif (gep_tipp == 2):
        gep_tipp = "papír"
    elif (gep_tipp == 3):
        gep_tipp = "olló"

    if (felhasznalo_tippje == gep_tipp):
        print("Döntetlen")
    elif (felhasznalo_tippje == "olló") and (gep_tipp == "papír"):
        print("Győztél")
    elif (felhasznalo_tippje == "olló") and (gep_tipp == "kő"):
        print("Vesztettél")
    elif (felhasznalo_tippje == "kő") and (gep_tipp == "papír"):
        print("Vesztettél")
    elif (felhasznalo_tippje == "kő") and (gep_tipp == "olló"):
        print("Nyertél")
    elif (felhasznalo_tippje == "papír") and (gep_tipp == "olló"):
        print("Vesztettél")
    elif (felhasznalo_tippje == "papír") and (gep_tipp == "kő"):
        print("Nyertél")
