import os
import secrets

from colorama import Fore
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64


#
# Autor   ->  an0mal1a
# Name    ->  Pablo
# GitHub  ->  https://github.com/an0mal1a
# Correo  -> pablodiez024@proton.me
#

def init_decrypt_file(file, key):
    try:
        with open(file, "rb") as f:
            content = f.read()

        key = gen_256(key.encode())
        decrypted_file_data = decrypt(content)

        print(decrypted_file_data, " | ", key, "\n")
        with open(file, "wb") as f:
            f.write(decrypted_file_data)

        return decrypted_file_data
    except ValueError:
        return 1

def init_crypt_file(file, key):
    with open(file, "rb") as f:
        content = f.read()

    if not key:
        key = secrets.token_bytes(32)

    else:
        # Generamos clave y la encriptamos
        key = key.encode()
        key = gen_256(key)

    encrypted_file_data = encrypt(content, key)
    with open(file, "wb") as f:
        f.write(key + encrypted_file_data)

    return encrypted_file_data, key


def gen_256(key):
    salt = base64.b64decode(b'azR5cDcwLlM0bHRJbmQ0dA==')
    #salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(key)
    return key


def decrypt(encrypted_data):
    key = encrypted_data[:32]
    init_vector = encrypted_data[32:48]
    ciphertext = encrypted_data[48:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(init_vector), backend=default_backend())
    decryptor = cipher.decryptor()
    message = decryptor.update(ciphertext) + decryptor.finalize()
    return unpad(message)


def encrypt(content, key):
    message = pad(content)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message) + encryptor.finalize()
    return iv + ciphertext


def pad(message):
    padder = padding.PKCS7(128).padder()
    padded_message = padder.update(message)
    padded_message += padder.finalize()
    return padded_message


def unpad(message):
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_message = unpadder.update(message)
    unpadded_message += unpadder.finalize()
    return unpadded_message


if __name__ == "__main__":
    try:
        ip = input("Enter IP >> ")

        with open("test.txt", "w") as test:
            test.write(ip)

        init_crypt_file("test.txt", "")

        with open("test.txt", "rb") as f:
            content = f.read()

        print("\nRESULT --> ", content)
        encrypted_file_data = decrypt(content)
        os.remove("test.txt")
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] EXITING PROGRAM...")
        exit()

