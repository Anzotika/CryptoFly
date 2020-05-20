# CryptoFly 
![CryptoFly Windows](/designer/CryptoFly.PNG)

## Used ciphers
All used ciphers in this project are symmetric block ciphers; a single key is used for encryption and decryption. 

- AES AES is an iterative rather than Feistel cipher. It is based on ‘substitution–permutation network’. It comprises of a series of linked operations, some of which involve replacing inputs by specific outputs (substitutions) and others involve shuffling bits around (permutations).
Interestingly, AES performs all its computations on bytes rather than bits. Hence, AES treats the 128 bits of a plaintext block as 16 bytes. These 16 bytes are arranged in four columns and four rows for processing as a matrix −
Unlike DES, the number of rounds in AES is variable and depends on the length of the key. AES uses 10 rounds for 128-bit keys, 12 rounds for 192-bit keys and 14 rounds for 256-bit keys. Each of these rounds uses a different 128-bit round key, which is calculated from the original AES key.
- Blowfish was designed as an alternative to DES. Blowfish has a 64-bit block size and a variable key length from 32 bits up to 448 bits. It is a 16-round Feistel cipher and uses large key-dependent S-boxes. In structure it resembles CAST-128, which uses fixed S-boxes.

![Blowfish algorithm](https://en.wikipedia.org/wiki/Blowfish_(cipher)#/media/File:Blowfish_diagram.png)

- Twofish has a block size of 128 bits, and accepts a key of any length up to 256 bits. The cipher is a 16-round Feistel network with a bijective function made up of four key dependent 8-by-8 bit Sboxes, a fixed 4-by-4 maximum distance seperable matrix, a pseudo Hadamard transform, bitwise rotations, and a
carefully designed key schedule.

![Twofish algorithm](https://en.wikipedia.org/wiki/Twofish#/media/File:Twofishalgo.svg)
