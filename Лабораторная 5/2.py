a = input("Введите пароль: ")
if len(a) > 8:
    if any(cifra.isdigit() for cifra in a):
        if any(BUKVA.isupper() for BUKVA in a):
            print("Пароль надежен")
        else:
            print("Пароль слаб")
    else:
        print("Пароль слаб")
else:
    print("Пароль слаб")