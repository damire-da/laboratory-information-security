from functions import decryption, reading, writing

ciphertext = reading()
voc = [' и ',' в ',' не ',' на ',' что ',' по ',' к ',' но ',' у ',' как ']

def finding(word, ciphertext):
    pass
    for word in voc:
        key = finding(word, ciphertext)
        if key != None:
            print(decryption(key, ciphertext))
            break