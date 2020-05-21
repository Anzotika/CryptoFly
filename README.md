# CryptoFly

This project was made for assignment in BONEVET/(I) class of python 2020
## The program itself
It is made for encrypting and decrypting files such as pdf, random files, images etc.

![CryptoFly Windows](/designer/CryptoFly.PNG)

## How the program works
Depending on whether you want to encrypt or decrypt your file, you have to follow the steps below.
1.	For encryption you have to choose the type of the algorithm you wish to continue. (For decryption you have to choose the type of the algorithm you encrypted the file with)
2.	The key for encryption/decryption is a key which in our program is related to PASSWORD
3.	You upload the file.

After finishing everything you press the button and to be sure that your file is encrypted/decrypted a new window pops up to tell you that everything is finished.

![Confirmation Window](/designer/confirmation.PNG)

The file is always saved in the location that you already have the base file (file that is yet to be encrypted nor decrypted).

## Used ciphers
All used ciphers in this project are symmetric block ciphers; a single key is used for encryption and decryption.

- AES AES is an iterative rather than Feistel cipher. It is based on ‘substitution–permutation network’. It comprises of a series of linked operations, some of which involve replacing inputs by specific outputs (substitutions) and others involve shuffling bits around (permutations).
Interestingly, AES performs all its computations on bytes rather than bits. Hence, AES treats the 128 bits of a plaintext block as 16 bytes. These 16 bytes are arranged in four columns and four rows for processing as a matrix −
Unlike DES, the number of rounds in AES is variable and depends on the length of the key. AES uses 10 rounds for 128-bit keys, 12 rounds for 192-bit keys and 14 rounds for 256-bit keys. Each of these rounds uses a different 128-bit round key, which is calculated from the original AES key.
- Blowfish was designed as an alternative to DES. Blowfish has a 64-bit block size and a variable key length from 32 bits up to 448 bits. It is a 16-round Feistel cipher and uses large key-dependent S-boxes. In structure it resembles CAST-128, which uses fixed S-boxes.

- Twofish has a block size of 128 bits, and accepts a key of any length up to 256 bits. The cipher is a 16-round Feistel network with a bijective function made up of four key dependent 8-by-8 bit Sboxes, a fixed 4-by-4 maximum distance separable matrix, a pseudo Hadamard transform, bitwise rotations, and a
carefully designed key schedule.

## Warning
The password should be remembered by the user and the user should be really careful while writing it.

## Members
[Anzotikë Bilalli](https://github.com/Anzotika)

[Arbena Musa](https://github.com/ArbenaMusa)
