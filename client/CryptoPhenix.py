import os
import re
import secrets
import colorama
from colorama import Fore
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

colorama.init()


def init_decrypt_file(file):
    with open(file, "rb") as f:
        content = f.read()
    print(content)

    encrypted_file_data = decrypt(content)

    print(f"\n[!] --> decripted content:\n {encrypted_file_data}")
    with open(file, "wb") as f:
        f.write(encrypted_file_data)


def init_crypt_file(file):
    with open(file, "r") as f:
        content = f.read()

    # Print contenido del archivo
    print("[*] File content:\n" + content)

    # Generamos clave y la encriptamos
    key = secrets.token_bytes(32)
    decrypted_file_data = encrypt(content, key)

    print(f"[!] --> Encripted content:\n {decrypted_file_data}")

    with open(file, "wb") as f:
        f.write(key + decrypted_file_data)



def decrypt(encrypted_data):
    key = encrypted_data[:32]
    init_vector = encrypted_data[32:48]
    ciphertext = encrypted_data[48:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(init_vector), backend=default_backend())
    decryptor = cipher.decryptor()
    message = decryptor.update(ciphertext) + decryptor.finalize()
    return unpad(message)


def encrypt(content, key):
    message = pad(content.encode())
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


"""def security():
    times_to_crypt = None

    while not times_to_crypt:
        times_to_crypt = input('\t[!] Set dificult level [1-5] ---> ')
        try:
            times_to_crypt = int(times_to_crypt)
            if times_to_crypt > 5:
                print("[!] Error, opción no válida...")
                times_to_crypt = None
            else:
                return times_to_crypt
        except ValueError:
            print("[!] Error, opción no válida...")
            times_to_crypt = None"""


"""def open_crypt_file(file):
    with open(file, "rb") as f:
        content = f.read()
    print(content)
    key = secrets.token_bytes(32)
    encrypted_file_data = encrypt_file(content, key)

    print(f"\n[!] --> re encripted content:\n {encrypted_file_data}")
    with open(file, "wb") as f:
        f.write(encrypted_file_data)"""


def functions():
    print(Fore.BLUE + "[♦]" + Fore.YELLOW + " Que herramienta quieres utilizar?")
    print(Fore.YELLOW + "-" * 50)
    print(Fore.BLUE + 'A:' + Fore.YELLOW + ' --> Encrypt' + '\n \n'
          + Fore.BLUE + 'B:' + Fore.YELLOW + ' --> Decrypt.\n\n')
# + Fore.BLUE + 'C: ' + Fore.YELLOW + '--> Host Discovery\n')

    fun = None
    while not fun:
        fun = input(Fore.YELLOW + "         ╚═► ")
        if fun.lower() in ['a']:
            file = file_to_moddify()
            # times = security()

            # for time in range(times):
            init_crypt_file(file)

        elif fun.lower() in ['b']:
            file = file_to_moddify()
            init_decrypt_file(file)


def prove():
    file = input('[!] Introduce el archivo a encriptar -> ')

    init_crypt_file(file)
    input('[!] Encriptacion hecha! \n[ENTER] PARA DESENCRIPTAR')
    init_decrypt_file(file)
    input('[!] Desencriptacion hecha! \n[ENTER] PARA SALIR')
    exit()


def file_to_moddify():
    file = None

    while not file:
        file = input(
            Fore.YELLOW + "\n\t[!] " + Fore.GREEN + "Introduce el archivo a des\encriptar >>> ")
        ext = re.findall("\.([a-z]+)$", file)

        if ext:
            try:
                with open(file, "rb"):
                    pass
                return file
            except Exception as e:

                print(Fore.RED + "\nERROR --> ", e, Fore.RESET)
                file = input(
                    Fore.YELLOW + "\n\t[!] " + Fore.GREEN + "Introduce el archivo a encriptar >>> ")
        else:
            print(Fore.RED + "[!] Tienes que intoducir la extensión del archivo")
            file = None
    file = input(' -> ')
    return file


if __name__ == "__main__":
    while True:
        try:
            functions()
        except KeyboardInterrupt:
            print(Fore.RED + "\n[!] EXITING PROGRAM...")
            exit()
