
# mesaj parametresini iste ve print et
# Eğer mesaj parametresi girilmezse program hata verir!
def yaz(mesaj):
    print("Yaz fonksiyonundan ",mesaj)

yaz("Merhaba")

print("\n")


# Eğer isim ve yaş değişkenen değer atanmazsa 'bilinmiyor' ata.
# Eğer ogrenciMi değişkenen değer atanmazsa False ata.
# Dolayısıyla bu paremetleri girmek opsiyoneldir.
def yazdir(isim = 'bilinmiyor', ogrenciMi = False, yas = 'bilinmiyor'):
    print("""
       İsim: {}
       Yas: {}
       Ogrenci mi? {}
    """.format(isim, yas, ogrenciMi))

    
# Normalde parametreleri sıralı bir şekilde belirtisiniz
# Fakat ogrenciMi paremetresini girmek istemeyip yas parametresini girmek istiyorsunuz
# O zaman yas = 'deger' diyip parametre adını belirtmeniz gerekir.
yazdir('Aydın', yas = 14) 

print("\n")


# Matematikte fonksiyon: f(x) = x + 2
# f -> fonksiyon adı
# x -> paremetre
# x + 2 -> sonuç

# Python'da fonksiyon:
#  def f(x):
##   return x + 2

## yani sonuç 'return' ile döndürülür 

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