## İşlem önceliği

print("2 * 4 / (3 + 5) = ", 2 * 4 / (3 + 5))

print("\n\n")

## Aritmetik Operatörler

print("Aritmetik Opetörler: ")

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

print("Atama operatörleri")

x = 0
x += 2
print("x += 2:", x)

print("\n")


## Karşılaştırma operatörleri

print("Karşılaştırma operatörleri")

print("1 == 2?", 1 == 2) # Eşit mi
print("1 != 4?", 1 != 4) # Eşit değil mi
print("-2 < 4?", -2 < 4) # Küçük mü
print("0 > 0?", 0 > 0) # Büyük mü
print("3 <= -1? ", 3 <= -1) # Küçük veya eşit mi
print("4 >= 4? ", 4 >= 4) # Büyük veya eşit mi

print("Elma == Elma?", 'Elma'=='Elma')

print("\n")

## Mantık Operatörleri

print("Mantık operatörleri")

print("4 > 2 ve 0 == 1?", 4 > 2 and 0 == 1) # Ve bağlacı
print("True veya Elma==Armut?", True or ('Elma' == 'Armut')) # Veya bağlacı
print("1 == 0 değili?", not 1 == 0 ) # Değili bağlacı

print("\n")