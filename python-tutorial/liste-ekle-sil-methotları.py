
yemekler = ["Hamburger", "Pizza", "Nohut"]
liste = ['araba', 0, "3.14", -1, 3j, "erik", True, "kiraz"]
print(liste)
print("\n\n")
## Ekleme methotları

liste.append(2.71) # listenin sonuna eleman ekle.
liste.insert(1, "BMW") # 1. indisteki elemanı BMV ile değiştir.
liste.extend(yemekler) # yemeklerin elementlerini liste2'ye ekle

## Silme methotları

liste.remove("erik") # Erik'i listeden sil.
liste.pop(1) # 1. indisteki elemanı sil
del liste[1] # 1. indisteki elemanı sil

liste.clear() #  Listedeki elemanları temizle
print("Yeni liste, ekleme ve silmeler yapıldı:", liste)
del liste # Liste değişkenini sil