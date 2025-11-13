a = input("Введите текст: ")
if a.find("SECRET") != -1:
    b = a.replace("SECRET","******")
    print(b,"Предупреждение")
else:
    print("Cообщение о безопасности")