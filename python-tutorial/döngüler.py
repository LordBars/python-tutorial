

# range(p1, p2, p3)
# 1. parametre: Başlangıç noktası (Başlangıç noktası dahil)
# 2. paremetre: Bitiş noktası (Bitiş noktası dahil değil)
# 3. parametre: her adımda i'nin kaç artacağını söyler. Belirtmezseniz 1 olarak kabul edilir.
for i in range(1, 14, 2):

    if i == 7:
        break # break döngüden tamamen çıkar. Yani 9, 11, 13 sayıları print edilmeyecektir.
    if i == 3:
        continue # continue mevcut tekrarlamayı atlar. Yani sadece 3 sayısı print edilmeyecektir

    print("Adım:", i)

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
