# cript Cesar
def encrypt(text, key):
    text = text.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted_message = ""
    for letter in text:
        if letter in alpha:
            letter_index = (alpha.find(letter) + key) % len(alpha)
            encrypted_message += alpha[letter_index]
        else:
            encrypted_message += letter
    return encrypted_message


res = encrypt("Hello you", key=3)
print(res)


# ?????