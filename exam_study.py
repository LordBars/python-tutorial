# Python yorumlanan bir dildir.
# Kodlar satır satır okunur.
# .py uzantısı vardır

### Değişkenler

## Sayısal veri tipleri

a = 2 # int
b = 4.0 # float
c = 1j # Complex

print("A:" , a, "\n", type(a))
print("B:" , b, "\n", type(b))
print("C:" , c, "\n", type(c))

print("\n")

## String'ler

string = 'Merhaba'
string = "Merhaba"
string = """ Merhaba ben uzun string
            satırları atlayabilirim """
print("string: ", string, "\n", type(string))

print("\n")

## Boolean

bool1 = True
bool1 = False
print("bool:", bool1, "\n", type(bool1))

print("\n")


## None: Bir değişkenin değeri ve tipi olmadığını ifade eder.

none1 = None # Değer ve tip bilinmiyor
print("none1:", none1, "\n", type(none1)) 

print("\n\n")

## İşlem önceliği (Matematik kuralları ile aynı)

print("2 * 4 / (3 + 5) = ", 2 * 4 / (3 + 5))

print("\n\n")

## Aritmetik Operatörler

print("8 + 1:", 8 + 1) # Toplama
print("5 - 1:", 5 - 1) # Çıkarma
print("2 * 4:", 2 * 4) # Çarpma
print("6 / 3:", 6 / 3) # Kalansız Bölme
print("2 ** 3:", 2 ** 3) # Üssünü alma
print("10 % 3:", 10 % 3) # Mod (Kalan) bulma
print("10 // 3:", 10 // 3) # Bölüm bulma 

print("\n\n")

### !!!! DİKKAT: Kalansız bölme (/) işlemi her zaman 'float' tipinde değer döndürür
print(""" 
!!!! DİKKAT: Kalansız bölme (/) işlemi 
her zaman 'float' tipinde değer döndürür (4/2):""", type(4 / 2))

print("\n")

## Atama Operatörleri
### x +=2 => x = x + 2 demektir. 
### Yukarıdaki operatörler (+, -, *, **, %, ...) aynen burada kullanılabilir. 
### Örneğin: +=, -=, *=, /=, %=, **=, ...

x = 0
x += 2
print("x += 2:", x)

print("\n")


## Karşılaştırma operatörleri

print("1 == 2?", 1 == 2) # Eşit mi
print("1 != 4?", 1 != 4) # Eşit değil mi
print("-2 < 4?", -2 < 4) # Küçük mü
print("0 > 0?", 0 > 0) # Büyük mü
print("3 <= -1? ", 3 <= -1) # Küçük veya eşit mi
print("4 >= 4? ", 4 >= 4) # Büyük veya eşit mi

print("Elma == Elma?", 'Elma'=='Elma')

print("\n")

## Mantık Operatörleri

print("4 > 2 ve 0 == 1?", 4 > 2 and 0 == 1) # Ve bağlacı
print("True veya Elma==Armut?", True or ('Elma' == 'Armut')) # Veya bağlacı
print("1 == 0 değili?", not 1 == 0 ) # Değili bağlacı

print("\n")

## Anahtar noktalar:
### "1" + 2 --> Hata, str int ile toplanamaz
### "1" - 2 --> Hata, str int ile çıkarılamaz
### "1" / 2 --> Hata, str int ile bölünemez
### "1" * 2 --> Kabul, str ile int çarpılabilir, sonuç: "11" (str tipinde) olur.
### "1" * 2.0 --> Hata, str ile float çarpılamaz.
print("'1' * 2: ", "1" * 2)

print("\n\n")

## Tip dönüşümleri

a = str(2) # a: '2' str
b = float(2) # b: 2.0 float 
c = int('2') # c: 2 int

print("\n\n")

## print fonksiyonu

print('Merhaba Dünya ben Mars')
print("Merhaba", "Dünya", "Ben", "Mars", sep="\n") # argümanları ayırır
print("Merhaba", end= "\n...\n...\n...\n...\n") # printin sonundaki değeri değiştirir, normalde satır atlama (\n)
print("Dünya Ben Mars.", end="\n\n")

print("\n\n")

## input fonksiyonu

giris = input("Bir şey giriniz: ")
print("Girdiğiniz şey:", giris)

print("\n\n")

## if-elif-else

ad = input("Adınız (ipucu: python): ")
parola = input("Parolanız (ipucu: 123): ")
if ad == 'python' and parola == '123':
    print("Bravo!")

elif ad == 'python':
    print('Parolan hatalı')

elif parola == '123':
    print("Adın hatalı")

else:
    print("Hem adın hem de kullanıcı adın yanlış LOL")

print("\n\n")

### Listeler
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
### Liste Methotları

yemekler = ["Hamburger", "Pizza", "Nohut"]
liste2 = ['araba', 0, "3.14", -1, 3j, "erik", True, "kiraz"]
print(liste2)
print("\n\n")
#### Ekleme methotları

liste2.append(2.71) # listenin sonuna eleman ekle.
liste2.insert(1, "BMW") # 1. indisteki elemanı BMV ile değiştir.
liste2.extend(yemekler) # yemeklerin elementlerini liste2'ye ekle

#### Silme methotları

liste2.remove("erik") # Erik'i listeden sil.
liste2.pop(1) # 1. indisteki elemanı sil
del liste[1] # 1. indisteki elemanı sil

liste2.clear() #  Listedeki elemanları temizle
print("Yeni liste, ekleme ve silmeler yapıldı:", liste2)
del liste2 # Liste değişkenini sil

print("\n\n")

### Sorting, ters çevirme ve kopyalama methotları
meyveler = ["portakal", "elma", "muz", "kiraz", "erik", "ayva"]
print("Meyveler:", meyveler)
meyveler.sort()
print("Sıralanmış Meyveler:", meyveler)
meyveler.reverse()
print("Ters çevrilmiş Meyveler:", meyveler)

print("\n")

meyveler_kopya = meyveler.copy()
meyveler_referans = meyveler

meyveler[1] = "ananas"
print("Meyveleri değiştirdim: ",meyveler)
print("meyveler_referans değişkeni de beraberinde değişti: ", meyveler_referans)
print("Ama bakın, copy() methodunu kullanınca değişiklik meyveler_kopya listesine yansımadı:", meyveler_kopya)

print("\n\n")

## String'ler

string = '   Merhaba, Dünya  '
print("String'ler listedir. Elemanlara erişebilir ve değişterebilirsiniz")
print(string)
print("string[6]:", string[6])
print("len(string):", len(string))
print("Merhaba in string:", 'Merhaba' in string)
print("Merhaba not in string:", 'Merhaba' not in string)
print("string.upper():", string.upper())
print("string.lower():", string.lower())
print("string.strip():", string.strip())
print("string.split(','):", string.split('j'))
print("string.replace('Dünya', 'Mars'):", string.replace('Dünya', 'Mars'))
print("string + ' Ben Jüpiter':", string + "Ben Jüpiter")

form = """ 
  İsim = {}
  Yaş = {}
  Şifre = {} """.format('Python', '30', '123')

print(".format() fonksiyonu ile bilgi doldurma:\n", form)

print("\n\n")

## Döngüler

for i in range(1, 10):
    print("Adım:",i)

print("\n\n")

while True:
    print("""Sonsuz Döngüye hoşgeldin, çıkışı doğru odadan geçerek bul.
    1 aydır yemek yememiş devasa aslanın odası için 1 yaz
    Zehirli Sarmaşıklarla dolu oda için 2 yaz
    150 derecelik oda için 3 yaz
    Her yeri bubi tuzaklık oda için 4 yaz
    """)
    yanit = input("Yanıtınız: ")
    if yanit == '1':
        print("Doğru yanıt!")
        break
    if yanit == '2':
        print("Zehirlendin :(, tekrar dene")
    if yanit == '3':
        print("Çok sııııcakkk, tekrar dene...")
    if yanit == '4':
        print("2. adımınında tuzağa yakalandın, tekrar dene...")

print("\n\n")

# Liste yinelemesi

urunler = ['MacBook Pro', 'Pythoncı klavyesi', 'Airpad', 'Samsung Galaxy Note 10']

for urun in urunler:
    print(urun)

print("\n\n")

# String yinelemesi

string = 'merhaba'
for karakter in string:
    print(karakter)

print("\n\n")
## Fonksiyonlar

def yaz(mesaj):
    print("Yaz fonksiyonundan ",mesaj)

yaz("Merhaba")

print("\n")

def yazdir(isim = 'bilinmiyor', yas = 'bilinmiyor', ogrenciMi = False):
    print("""
       İsim: {}
       Yas: {}
       Ogrenci mi? {}
    """.format(isim, yas, ogrenciMi))

    
yazdir(yas = 14, ogrenciMi = True)

print("\n")

def asal_sayi_mi(sayi):

    if sayi < 1:
        return "Hatalı sayı girdin"

    if sayi == 1:
        return False

    for i in range(sayi - 1, 1, -1):
        if sayi % i == 0:
            return False

    return True

sayi = int(input("Sayı giriniz: "))
sonuc = asal_sayi_mi(sayi)
print(sayi, "Asal sayi mi? ", sonuc)