import os
from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)

if not os.path.exists("key.key"):
    write_key()
def load_key():
    with open("key.key", "rb") as f:
        key = f.read()
    return key
key = load_key()
fernet = Fernet(key)
def write_password():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    with open("passwords.txt", "w") as f:
        f.write(f"{login}|{fernet.encrypt(password.encode()).decode()}\n")
write_password()
def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            login,password = data.split("|")
            print(f"Логин: {login} | Пароль: {fernet.decrypt(password.encode()).decode()}")
while True:
    choise = int(input("Добавить новые данные - 1\nПосмотреть все данные - 2\nВыход - 3: "))
    if choise == 1:
        write_password()
    elif choise == 2:
        view()
    elif choise == 3:
        break

