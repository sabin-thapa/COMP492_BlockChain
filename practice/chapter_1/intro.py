# Symmetric Encryption

#importing fernet library for random key gen for symmetric encryption
from cryptography.fernet import Fernet

msg = 'Hello, World!'

key = Fernet.generate_key()

# Instantiate the class with the encryption key 
fernet = Fernet(key)

#Encrypting the string using fernet. 
#First, need to encode to byte string before encryption

encryptMsg = fernet.encrypt(msg.encode())

print(f'Original msg: {msg} \nEncrypted Msg: {encryptMsg}')

#Decryption using the same key

decryptMsg = fernet.decrypt(encryptMsg).decode()
print(f'Decrypted Msg: {decryptMsg}')

#Substitution Cipher - Caesar Cipher    
# Caesar cipher is a method in which each letter is rotated by three letters

def encrypt(text, shift):
    result = ''

    #traverse the text
    for i in range(len(text)):
        char = text[i]

        #Uppercase
        if (char.isupper()):
            # The ord() function returns the number representing the unicode code of a specified character.
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif(char.islower()):
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += chr((ord(char)))
    return result

def decrypt(text, shift):
    result = ''

    #traverse the text
    for i in range(len(text)):
        char = text[i]

        #Uppercase
        if (char.isupper()):
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif(char.islower()):
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += chr((ord(char)))
    return result

inputText = 'Hello, folks!!'
shift = 4
print ("Original String  : " + inputText)
print ("Shift : " + str(shift))
encryptMessage = encrypt(inputText,shift)
print ("Encrypted String: " + encryptMessage)
decryptMessage = decrypt(encryptMessage, shift)
print ("Decrypt String: " + decryptMessage)

#Assymetric Encryption
#RSA

def rsa():
    import rsa

    publicKey, privateKey = rsa.newkeys(512)

    textMessage = 'RSA Assymetric Encryption Practice'

    encryptedMsg = rsa.encrypt(textMessage.encode(), publicKey)

    decryptedMsg = rsa.decrypt(encryptedMsg, privateKey).decode()

    print("Original string: ", textMessage)
    print("Encrypted string: ", encryptedMsg)
    print("decrypted string: ", decryptedMsg)

rsa()