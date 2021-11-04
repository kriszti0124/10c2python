from random import *


def listaAlapok():
    #lista létrehozása
    alapok=[]
    for i in range(10):
        alapok.append(randint(1,50))
    alapok.append('alma')
    alapok.append('szilva')
    print(alapok)
    #lista kiírása szépen
    for item in alapok:
        print(item, end=" ")
    print()
    print(alapok[4])   #a négyes indexű elem
    print(len(alapok)) #lista elemszáma
    alapok.insert(4, 'körte') #elem beszúrása az adott helyre
    print(alapok.index('körte')) #az elem indexe
    #print(alapok.index(55)) hibaüzenettel áll meg
    alapok.remove('körte')
    alapok.pop()
    del alapok[-1] #az utolsó törlése
    del alapok[1] #az egyes indexű elem törlése
    #alapok.clear() a lista elemeket törli
    #del alapok a listát törli
    alapok.reverse() #sorrendet megforditja
    alapok.sort() #növekvő sorrendbe teszi
    alapok.reverse()
    print()
    print(alapok[5:]) # 5ös index
    print()
    print(alapok[4:]) #elejétől az adott indexű elemig
    print(alapok[-1]) #utolsó
    print(alapok[-2]) #utolsó előtti
    print(alapok[-2:]) #utolsó kettő
    print(alapok[3:5])
    alapok[6]= 'narancs'
    for item in alapok:
        print(item, end=" ")
    print()

def feladat1():
    elemszam= int(input("Add meg az elemek számát!"))
    szamok=[]
    for i in range(elemszam):
        szamok.append(randint(1,50))
        print(szamok)
        paratlandb=0
        for item in szamok:
            if item%2==1:
                paratlandb+1 #paratlandb= paratlandb+1
        print('A páratlanok száma',paratlandb)

def feladat2():
      elemszam= int(input("Add meg az elemek számát!"))
    szamok=[]
    for i in range(elemszam):
        szamok.append(randint(1,50))
        print(szamok)
        paratlandb=0
        for item in szamok:
            if item%2==0:
                osszeg+item
        print("A párosok összege", osszeg)

def feladat3():
    for i in range(elemszam):
        szamok.append(randint(1,50))
    print(szamok)
    for i in range(len(szamok)):
        if szam[i]%2==0:
            print(i, '/t' ,szamok[i])




#listaAlapok()
#feladat1()
#feladat2()