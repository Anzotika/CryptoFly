from twofish import Twofish


def twofish_encrypt(password, path):
    infile = open(path, "r")
    data = infile.read()
    infile.close()

    if len(data) % 16:
        nstr = str(data + "%" * (16 - len(data) % 16)).encode('ascii')
    else:
        nstr = data.encode("ascii")

    cipher = Twofish(bytes(password, 'ascii'))
    encrypted = b''

    for x in range(int(len(nstr) / 16)):
        encrypted += bytes(cipher.encrypt(nstr[x * 16: (x + 1) * 16]))

    outfile = open(path + '.encrypted', "wb")
    outfile.write(encrypted)
    outfile.close()


def twofish_decrypt(password, path):
    infile = open(path, "rb")
    data = infile.read()
    infile.close()

    cipher = Twofish(bytes(password, 'utf-8'))
    decrypted = b''  # decrypted string

    for x in range(int(len(data) / 16)):
        decrypted += cipher.decrypt(data[x * 16: (x + 1) * 16])

    outfile = open(path + '.decrypted', "wb")
    outfile.write(decrypted)
    outfile.close()