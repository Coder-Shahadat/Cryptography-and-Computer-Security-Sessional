# Poly_alphabetic cipher
def generateKey(plainText, keyword):
    key = ''
    for i in range(len(plainText)):
        key += keyword[i % len(keyword)]
    return key


def cipherText(plainText, key):
    cipher_text = ""
    for i in range(len(plainText)):
        shift = ord(key[i].upper()) - ord('A')
        new_char = chr((ord(plainText[i].upper()) + shift) % 26 + ord('A'))
        cipher_text += new_char.lower() if plainText[i].islower() else new_char
    return cipher_text


def decrypt(cipher_text, key):
    plainText = ''
    for i in range(len(cipher_text)):
        shift = ord(key[i].upper()) - ord('A')
        new_char = chr((ord(cipher_text[i].upper()) - shift + 26) % 26 + ord('A'))
        plainText += new_char.lower() if cipher_text[i].islower() else new_char
    return plainText


plainText = "Information"
keyword = "Ice"
key = generateKey(plainText, keyword)
cipher_text = cipherText(plainText, key)
print("Ciphertext :", cipher_text)
print("Decrypted Text :", decrypt(cipher_text, key))
