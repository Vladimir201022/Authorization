from main import load_key
key = load_key()
fernet = Fernet(key)
def authorization(login,password,fernet):
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            lgn,pwd = data.split("|")
            if login==lgn and password==fernet.decrypt(password.encode()).decode():
                return True
    return False
while True:
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    if authorization(login,password,fernet):
        print("Вы авторизованы")
        break
    else:
        print("Проверьте логин или пароль")

    