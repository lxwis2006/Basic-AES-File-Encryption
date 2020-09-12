import pyAesCrypt

bs = 64 * 1024
psw = input("Enter the PREVIOUSLY used password... or a new one: ")
choice = input("E/ENCRYPTION | D/DECRYPTION: ")

def encryptionmethod():
    pyAesCrypt.encryptFile(name_of_file, name_of_file + ".aes", psw, bs)

def decryptionmethod():
    pyAesCrypt.decryptFile(name_of_decrypt_file, "decrypted1.txt", psw, bs)

if choice == "E":
    name_of_file = input("Enter the NAME of the FILE u WANT to ENCRYPT: ")
    encryptionmethod()

if choice == "D":
    name_of_decrypt_file = input("Enter the NAME of the FILE u WANT to DECRYPT: ")
    decryptionmethod()
    