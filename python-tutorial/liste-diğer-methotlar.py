### Sorting, ters çevirme ve kopyalama methotları
meyveler = ["portakal", "elma", "muz", "kiraz", "erik", "ayva"]
print("Meyveler:", meyveler)

meyveler.sort()
print("Sıralanmış Meyveler:", meyveler)

meyveler.reverse()
print("Ters çevrilmiş Meyveler:", meyveler)

print("\n")

# Kopyalama ve referans olarak atama
# = sembolü ile atama yapılınca atayan değişkende değişiklik olduğunda
# atanan değişkendede değişiklik olur:
## x = 2 
## y = x
## x += 2
## y == x ? True (x 4 olunca y de 4 oldu)
# .copy() methotu ile kopyalanırsa, kopyalanan değişkende değişiklik olduğunda
# kopyalanmış değişkene yansımaz:
## x = 2
## y = x.copy()
## x += 2
## y == x ? False
meyveler_kopya = meyveler.copy()
meyveler_referans = meyveler

meyveler[1] = "ananas"
print("Meyveleri değiştirdim: ",meyveler)

print("meyveler_referans değişkeni de beraberinde değişti: ", meyveler_referans)
print("meyveler == meyveler_referans ?", meyveler == meyveler_referans)

print("Ama bakın, copy() methodunu kullanınca değişiklik meyveler_kopya listesine yansımadı:", meyveler_kopya)
print("meyveler == meyveler_kopya ?", meyveler == meyveler_kopya)
