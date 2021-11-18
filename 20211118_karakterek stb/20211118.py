def megtalal(karakterlanc,keresendo):
    if keresendo in karakterlanc:
        return karakterlanc.index(keresendo)
    else:
        return -1



def karakterszam(karakterlanc, megszamolando):
   # return.karakterlanc.count(megszamolando)

   def nagybetu():
       nagybetuk='AÁBCDEÉ'

def feladat2():
    szoveg='Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequatur, quis?'
    karakter=input('Adj meg egy karaktert!')
    #kiírjuk a vissza kapott eredményt
    print(megtalal(szoveg, karakter))
    #változóba tesszük
    eredmeny=megtalal(szoveg, karakter)
    if eredmeny==-1:
        print('A megadott karakter nem szerepel a szövegben')
    else:
        print('A megadott karakter a', eredmeny, 'indexű helyen fordul elő először.')


def feladat4():
    szoveg='Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequatur, quis?'
    karakter=input('Adj meg egy karaktert!')
    karakterszam(szoveg, karakter)
    print(' A megadott szövegben az adott karakter', karakterszam(szoveg, karakter), 'fordul elő.')

def feladat6():
    szoveg='Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequatur, quis?'
    print('A megadott szöveg', karakterszam(szoveg, ' ')+1 'szóból áll.')


def feladat5():
    prefixes='JKLMNOPQ'
    suffixe='ack'
    kacsak=[]
    for item in prefixes:
        kacsak.append(item+suffixe)
        for item in kacsak:
            print(item, end=' ')



#itt kezdődik a főprogram
#feladat2()
#feladat4()
#feladat6()
#feladat5()
# hf 7 8 10 