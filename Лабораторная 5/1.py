a = input("Введите имя:").strip()
if any(b.isalnum() for b in a):
    a = a.lower()
    print("Имя корректно: ",a)
else:
    print("Ошибка")