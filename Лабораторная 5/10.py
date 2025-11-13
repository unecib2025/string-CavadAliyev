a = input("Введите отчет: ").lower()
b = len(a.split("."))
print(b)
c = a.strip()
d = len(c)
print(d)
if a.startswith("report"):
    print("Начинаетcя с 'report'")
if a.count("erorr") >= 2:
    print("Ошибки найдены")
else:
    print("Ошибки не найдены")