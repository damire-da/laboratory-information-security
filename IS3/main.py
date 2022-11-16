# -*- coding: cp1251 -*-

from functions import encryption, decryption, reading, writing


def start():
    alpha = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя,. АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ!?:;'
    Key = int(input("Enter key: "))
    operation = input("Введите 'ш' для шифрования, 'р' для расшифрования: ")
    if operation == 'ш':
        PlainText = reading()
        CipherText = encryption(Key, PlainText, alpha)
        writing(CipherText, operation)
    elif operation == 'р':
        CipherText = reading()
        PlainText = decryption(Key, CipherText, alpha)
        writing(PlainText, operation)
    else:
        print("Выбрана неверная операция")


if __name__ == '__main__':
    start()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
