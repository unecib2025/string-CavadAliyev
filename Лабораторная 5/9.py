text = "login attempt failed access denied unauthorized access"
a = text.count("failed")
b = text.count("denied")
if a != -1 and b != -1:
    print("Попытка несанкционированного доступа")
