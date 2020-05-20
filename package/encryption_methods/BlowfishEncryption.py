import blowfish

bufferSize = 8

def blowfish_encrypt(password, path):
    cipher = blowfish.Cipher(bytes(password, 'ascii'))

    infile = open(path, 'rb')
    data = infile.read()
    infile.close()

    encrypted = b''

    for i in range(0, len(data), bufferSize):
        block = bytearray(data[i:(i + bufferSize)])

        if len(block) < bufferSize:
            for _ in range(bufferSize - len(block)):
                block.append(0)

        encrypted += cipher.encrypt_block(block)

    outfile = open(path + '.encrypted', 'wb')
    outfile.write(encrypted)
    outfile.close()


def blowfish_decrypt(password, path):
    cipher = blowfish.Cipher(bytes(password, 'ascii'))

    infile = open(path, 'rb')
    text = infile.read()
    infile.close()

    decrypted = b''

    for i in range(0, len(text), bufferSize):
        block = bytearray(text[i:(i + bufferSize)])

        if len(block) < bufferSize:
            for _ in range(bufferSize - len(block)):
                block.append(0)

        decrypted += cipher.decrypt_block(block)

    outfile = open(path + '.decrypted', 'wb')
    outfile.write(decrypted)
    outfile.close()