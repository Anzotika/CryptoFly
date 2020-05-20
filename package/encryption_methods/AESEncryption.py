import pyAesCrypt
from os import stat, remove

bufferSize = 16

def aes_encrypt(password, path):
    with open(path, 'rb') as infile:
        with open(path + '.encrypted', 'wb') as outfile:
            pyAesCrypt.encryptStream(infile, outfile, password, bufferSize)



def aes_decrypt(password, path):
    with open(path, 'rb') as infile:
        with open(path + '.decrypted', 'wb') as outfile:
            try:
                fileSize = stat(path).st_size
                print(fileSize)
                pyAesCrypt.decryptStream(infile, outfile, password, bufferSize, fileSize)
            except ValueError:
                remove(path + '.decrypted')