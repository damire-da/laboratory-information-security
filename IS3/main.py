from functions import encryption, decryption

def start():
    alpha = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
    Key = int(input("Enter key: "))
    operation = input("Введите 'ш' для шифрования, 'р' для расшифрования: ")
    if operation == 'ш':
        PlainText = input("Введите текст для шифрования: ").strip()
        CipherText = encryption(Key, PlainText, alpha)
        print("Шифротекст: " + CipherText)
    elif operation == 'р':
        CipherText = input("Введите текст для расшифрования: ").strip()
        PlainText = decryption(Key, CipherText, alpha)
        print("Исходный текст: " + PlainText)
    else:
        print("Выбрана неверная операция")


if __name__ == '__main__':
    start()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
