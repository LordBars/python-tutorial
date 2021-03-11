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