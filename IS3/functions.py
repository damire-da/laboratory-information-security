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


