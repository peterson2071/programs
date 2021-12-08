def cypher():
    strKey = input("Key number: ")
    try:
        key = int(strKey)
    except:
        print("Invalid Key")
        quit()

    plaintext = input("Enter text: ")
    cyphertext = " "

    for i in range(len(plaintext)):
        encrypt = plaintext[i]

        if (encrypt.islower()):
            cyphertext += chr((ord(encrypt) + key - 97) % 26 + 97)
        elif (encrypt.isupper()):
            cyphertext += chr((ord(encrypt) + key - 65) % 26 + 65)
        else:
            cyphertext += encrypt
    print('Cyphertext: ', cyphertext)


if __name__ == '__main__':
    cypher()
