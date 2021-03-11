## Listeler
### Herhangi bir tipte değeri (bool, str, float vs) tutabilirler. 
### Aynı eleman iki kez bulunabilir.

liste = ["elma", 2, True, None, 4.7, '3']
print("liste:", liste)

## Listede var mı?
print("'elma' in liste:", "elma" in liste)

## Liste uzunluğu
print("len(liste):", len(liste))

# Liste itemlerına erişmek
print("liste[2]:", liste[2])
print("liste[-1]:", liste[-1])
print("liste[1:4]:", liste[1:4])
print("liste[:4]:", liste[:4])
print("liste[2:]:", liste[2:])
print("liste[-4: -1]:", liste[-4:-1])
print("liste[1:5:2]:", liste[1:5:2])
print("liste[-5:-1:2]:", liste[-5:-1:2])

### Listedeki elemanları değiştirme

liste[0] = "armut" # 0. indisteki elemanı(elma) armut ile değiştir.     
liste[1:3] = [11, False] # 1 ve 2. indislerdeki elemanları değiştir.
liste[-2:-1] = "Yeni" # -2 ve -1. indislerdeki elemanları değiştir.

print("\n\n")
print("Yeni liste, değiştirmeler yapıldı:", liste)
print("\n\n")