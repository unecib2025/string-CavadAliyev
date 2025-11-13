a = input("Введите електронный адрес: ")
if a.find("@") != -1 :
    b = a.split("@")
    if a.endswith(".com"):
        print("Домен:", b[1])
    else:
        print("Некорректный адрес")
else:
    print("Некорректный адрес")