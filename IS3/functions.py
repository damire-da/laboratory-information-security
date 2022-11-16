def encryption(Key, PlainText, alpha):
    CipherText = ''
    for p in PlainText:
        CipherText += alpha[(alpha.index(p) + Key) % len(alpha)]
    return CipherText

def decryption(Key, CipherText, alpha):
    PlainText = ''
    for p in CipherText:
        PlainText += alpha[(alpha.index(p) - Key) % len(alpha)]
    return PlainText


def reading():
    source = input("Источник данных: \n 'к' - консоль \t 'ф' - файл \n")
    if source == 'к':
        data = input("Введите текст: ").strip()
        return data
    elif source == 'ф':
        filename = input("Название файла с данными в формате '*.txt': \n")
        with open(filename, 'r', encoding="utf8") as f:
            data = f.read()
        data = data.encode('cp1251').decode('cp1251')
        return data
    else:
        print("[-] Выбрана неверная операция")

def writing(data, operation):
    op = operationtype(operation)
    exit = input("Вид вывода данных: \n 'к' - консоль \t 'ф' - файл: \n")
    if exit == 'к':
        print("Результат: ", data)
    elif exit == 'ф':
        string = f"Файл для вывода результата {op} в формате 'имя.txt': \n"
        filename = input(string)
        with open(filename, 'w', encoding="utf-8") as f:
            for symbol in data:
                try:
                    f.write(symbol.encode("cp1251").decode("cp1251"))
                except:
                    print(symbol)
                    pass
        print("\n[+] Результат %s записан в файл %s" % (operationtype(operation), filename))
    else:
        print("[-] Выбрана неверная операция")


def operationtype(operation):
    sh = "шифрования"
    rsh = "расшифрования"
    if operation == "ш":
        return sh
    elif operation == "р":
        return rsh


