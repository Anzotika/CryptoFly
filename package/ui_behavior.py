from PySide2.QtCore import Slot
import package.encryption_methods.AESEncryption as aes
import package.encryption_methods.BlowfishEncryption as blowfish
import package.encryption_methods.TwofishEncryption as twofish


class Behavior():
    ed = ''
    method = ''
    path = ''
    password = ''

    @Slot()
    def encrypt(self):
        self.ed = 'encrypt'

    @Slot()
    def decrypt(self):
        self.ed = 'decrypt'

    @Slot()
    def password(self, passwod):
        self.password = passwod

    @Slot()
    def browse(self, path):
        self.path = path
        print(self.path)

    @Slot()
    def done(self, method, password):
        self.method = method
        self.password = password
        # if len(self.password) != 0 & len(self.path) != 0:
        #     self.crypto_action()
        # else:
        #     print('Nuk jane dhene te gjitha te dhenat!!!')
        if self.method == 0:
            print('aes')
            if self.ed == 'encrypt':
                aes.aes_encrypt(self.password, self.path)
            else:
                aes.aes_decrypt(self.password, self.path)
        elif self.method == 1:
            print('blowfish')
            if self.ed == 'encrypt':
                blowfish.blowfish_encrypt(self.password, self.path)
            else:
                blowfish.blowfish_decrypt(self.password, self.path)
        else:
            print('twofish')
            if self.ed == 'encrypt':
                twofish.twofish_encrypt(self.password, self.path)
            else:
                twofish.twofish_decrypt(self.password, self.path)