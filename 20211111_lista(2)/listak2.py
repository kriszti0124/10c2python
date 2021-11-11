def feladat1():
    t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    t2 = ['Január', 'Február', 'Március', 'Április', 'Május', 'Június', 'Július', 'Augusztus','Szeptember', 'Október', 'November', 'December']
    t3=[]
    for i in range(0, len(t1)):
        t3.append(t2[i])
        t3.append(t1[i])
        print(t3)
        print("szépen:")
       # for item in t3:
           # print(item, end=' ')
            #feladat2(t3)



def feladat2(eztirjukki):
    for item in eztirjukki:
        #print(item, end=' ')
        print()
        


lista=['alma', 'körte', 'szilva', 'banán', 'őszibarack', 'ananász']



def feladat3(legnagyobbatkeres):
    legnagyobb=max(legnagyobbatkeres)
    print(legnagyobb)

szamok=[32, 5, 12, 8, 3, 75, 2, 15]

def feladat4(szetvalogat):
    paros=[]
    paratlan=[]
    for item in szetvalogat:
        if item&2==0:
            paros.append(item)
        else:
            paratlan.append(item)
    print("Párosok:", end=' ')
    feladat2(paros)
    print("Páratlanok:", end=' ')
    feladat2(paratlan)


def feladat5(lista):
    HatnalRovidebb=[]
    HatvagyHosszabb=[]
    for item in lista:
        hossz=len(item)
        if hossz<6:
            HatnalRovidebb.append(item)
            else:
                HatvagyHosszabb.append(item)
    print('Hatnál rövidebb szavak:', end=' ')
    feladat2(HatnalRovidebb)
    print("Hat vagy annál hosszabb szavak:", end=' ')
    feladat2(HatvagyHosszabb)



def feladat6_1(szoveg):
    szo='elkelkáposztástalaníthatatlanságoskodásaitokért '
    print("A szöveg hossza", len(szoveg))
    darabok=[]
    for i in range(0, len(szoveg), 5):
        darabok.append(szoveg[i:i+5])
        darabok.reverse()
        feladat2(darabok)
        def feladat2(eztirjukki,elvalaszto):
        for item in eztirjukki:
        print(item, end=elvalaszto)
        print()
#feladat1()
#feladat2(lista)
#feladat3(szamok)
#feladat4(szetvalogat)
#feladat5(lista)
feladat6_1('elkelkáposztástalaníthatatlanságoskodásaitokért ')