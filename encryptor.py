import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(data):
    return data + b" " * (AES.block_size - len(data) % AES.block_size)

def encrypt_file(key, in_filename, out_filename=None):
    if not out_filename:
        out_filename = in_filename + ".enc"
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    with open(in_filename, 'rb') as f:
        plaintext = f.read()
    ciphertext = cipher.encrypt(pad(plaintext))
    with open(out_filename, 'wb') as f:
        f.write(iv + ciphertext)
    print(f"Encrypted '{in_filename}' to '{out_filename}'")

def decrypt_file(key, in_filename, out_filename=None):
    if not out_filename:
        out_filename = in_filename[:-4]
    with open(in_filename, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext).rstrip(b" ")
    with open(out_filename, 'wb') as f:
        f.write(plaintext)
    print(f"Decrypted '{in_filename}' to '{out_filename}'")