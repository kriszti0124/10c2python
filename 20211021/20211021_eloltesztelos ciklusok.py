def feladat24():
    szam=float(input("Kérek egy számot!"))
    while szam !=0:
        szam=float(input("Kérek egy másik számot! Kilépés a 0-val,"))

def feladat25():
    szam=float(input("Kérek egy pozitív számot! "))
    while szam<=0:
        szam=float(input("Nem pozitív számot adtál, add meg újra!"))

def feladat26():
    szam=float(input("Kérek egy számot!"))
    osszeg=szam
    while szam<10:
        szam=float(input("Adj meg egy másik számot!"))

        osszeg+=szam
    print("A beadott számok összege",osszeg)


















#itt kezdődik a főprogram
#feladat24()
#feladat25()
feladat26()