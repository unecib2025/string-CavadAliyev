a = input("Введите слово: ")
S = ""
i = 0
while i < len(a):
    b = ord(a[i])
    c = chr(b)
    S = c + S
    i = i + 1
    print(b)
print(f"Ваше слово наоборот:{S}")