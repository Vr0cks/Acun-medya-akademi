#Soru 1:Kullanıcının girdiği bir listede tekrarlanan elemanları ve kaç kez tekrar ettiklerini bulan bir  Python programı yazın.

def tekrarlanan_elemanlar(liste):
    return {x: liste.count(x) for x in set(liste) if liste.count(x) > 1}

liste = input("Liste elemanlarını boşlukla ayırarak girin: ").split()
print(tekrarlanan_elemanlar(liste))

#Soru 2: Kullanıcının girdiği bir sayı listesindeki en büyük ikinci sayıyı bulan Python programını yazın.

def ikinci_en_buyuk(liste):
    liste = list(set(liste))  # Tekrar edenleri kaldırır
    liste.sort()  # Küçükten büyüğe sıralar
    return liste[-2] if len(liste) > 1 else "İkinci en büyük sayı yok."

liste = list(map(int, input("Liste elemanlarını boşlukla ayırarak girin: ").split()))
print(ikinci_en_buyuk(liste))

#Soru 3:  Kullanıcının girdiği bir listeyi küçükten büyüğe ve büyükten küçüğe sıralayan bir Python programı yazın.

def sirala(liste):
    return sorted(liste), sorted(liste, reverse=True)

liste = list(map(int, input("Liste elemanlarını boşlukla ayırarak girin: ").split()))
print("Küçükten büyüğe:", sorted(liste))
print("Büyükten küçüğe:", sorted(liste, reverse=True))

#Soru 4: Kullanıcının girdiği listedeki her elemanı 2 ile çarparak yeni bir liste oluşturan bir Python programı yazın. 

def ikiyle_carp(liste):
    return [x * 2 for x in liste]

liste = list(map(int, input("Liste elemanlarını boşlukla ayırarak girin: ").split()))
print("Yeni liste:", ikiyle_carp(liste))

#Soru 5: Kullanıcının girdiği liste elemanlarını rastgele karıştıran bir Python programı yazın. 

import random

def karistir(liste):
    random.shuffle(liste)
    return liste

liste = input("Liste elemanlarını boşlukla ayırarak girin: ").split()
karistir(liste)
print("Karışık liste:", liste)