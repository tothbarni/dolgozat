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
        print(str(n_betu) * 3)