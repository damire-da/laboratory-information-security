# -*- coding: cp1251 -*-

from functions import encryption, decryption, reading, writing


def start():
    alpha = '��������������������������������,. �����Ũ��������������������������!?:;'
    Key = int(input("Enter key: "))
    operation = input("������� '�' ��� ����������, '�' ��� �������������: ")
    if operation == '�':
        PlainText = reading()
        CipherText = encryption(Key, PlainText, alpha)
        writing(CipherText, operation)
    elif operation == '�':
        CipherText = reading()
        PlainText = decryption(Key, CipherText, alpha)
        writing(PlainText, operation)
    else:
        print("������� �������� ��������")


if __name__ == '__main__':
    start()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
