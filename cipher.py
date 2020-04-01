import string
from random_word import RandomWords


def encrypt (text , shift):
    text.lower()
    encryptedstring = ""
    for i in text :
        charvalue = ord(i) +shift
        if ( charvalue > 122):
            charvalue = ord('a') + (charvalue -123)
            encryptedstring += chr(charvalue)

        else:
            encryptedstring += chr(charvalue)
    return encryptedstring


def create_list(length):
    r = RandomWords()
    list = []
    for i in range(int(length)):
        list.append(r.get_random_word())
    
    print(list)
    return list


if __name__ == "__main__":
    list = create_list(10)
    for text in list:
        shift = 7
        print(f'CIPHER: {encrypt(text,shift)} | ORIGINAL: {text} | LENGTH: {len(text)}')
