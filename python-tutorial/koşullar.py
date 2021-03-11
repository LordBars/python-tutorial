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


"""

# Üstteki kod elifler olmadan buna eşittir:

if ad == 'python' and parola == '123':
    print("Bravo!")

else:
    if ad == 'python':
        print('parolan hatalı')

    else:
        if parola == '123':
            print('Adın hatalı')

        else:
            print('Hem adın hem de kullanıcı adın yanlış LOL')
"""    