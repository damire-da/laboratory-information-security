def encryption(Key, PlainText, alpha):
    CipherText = ''
    for p in PlainText:
        CipherText += alpha[(alpha.index(p) + Key) % len(alpha)]
def decryption():