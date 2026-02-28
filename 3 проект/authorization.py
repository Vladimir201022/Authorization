from main import load_key
from cryptography.fernet import Fernet


def authorization(login,password,fernet):
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            lgn,pwd = data.split("|")
            if login==lgn and password==fernet.decrypt(pwd.encode()).decode():
                return True
    return False


def main():
    key = load_key()
    fernet = Fernet(key)
    while True:
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        if authorization(login,password,fernet):
            print("Вы авторизованы")
            break
        else:
            print("Проверьте логин или пароль")


if __name__ == '__main__':
    main()