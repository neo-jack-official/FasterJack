![alt text](https://raw.githubusercontent.com/neo-jack-official/FasterJack/master/vista01.png)
# FasterJack para Python 3 (fasterjack.py)
# Es una Herramienta de denegacion para Servidores-Web por Neo-Jack FEB/2020

## ¿Qué es FasterJack?
En esta version, hemos querido pasar de una aplicacion simple a algo un poco mas sofisticado de forma sutil.
En la prectica es uan herramienta de denegacion o testeo de stress para sitios web.
La complejidad del programa se basa en la interaccion con sus subprogramas internos.
Lo que permiten un mejor control de cada aspecto del funcionamiento, con notificaciones de los procesos.
Incorpora dentro de sus funciones:
Mayor y mas eficientes Agentes de Navegacion que se asignan automaticamente en cada conexion y re-conexion del cliente.
Permitiendo una eficiencia mayor, y taza de deteccion inferior. Lo que hace requerir menos clientes al minuto de usar el programa.
en un rango de 30 a 115 clientes.
El paquete a enviar que en el fondo es un simple mensage que da instruciones al servidor, parcialmente editable en header.txt 
Bots Verificadores, que se ejecutan al comienzo para validar el sitio web o puerto, reduciendo fallos o uso del progrma en modo fantasma. Modo fantasma es cuando crees estar usando el programa en un servidor pero nunca fue de esa manera.
Tambien contiene opcion a acceso al Socket5 o conexion TOR, para su seguridad. con verificador de IP, para evitar uso fantasma de proteccion.
Implementa el nuevo sistema de conexion socket.socket(socket.AF_INET, socket.SOCK_STREAM) ya testeado en HostJack que a demostrado mayor eficiencia a la conexion y bloqueos.
Tambien se incorpora Bot Metodos lo que permite utilizar el programa en GET, POST o RANDOM por defecto.
Como es usual en este tipo de aplicaciones utiliza un minimo de ancho de banda, lo que es muy util para no agotar nuestra capacidad de Internet.

##Como Funciona FasterJack
FasterJack envia un paquete (encabezado) por cada cliente, con datos falsos pero que el servidor pueda reconocerlos como validos pero incompletos, al generar una conexion.
Por lo Cual el Servidor quedara a la espera del resto del encabezado que el cual nunca llegara.
los Servidores por lo general estan configurados por defecto a esperar 120 segundos aproximandamente por cliente que envie el paquete.
Lo cual causa que cada cliente agote los recursos lógicos del servidor, hasta que se satura y falla.

## Que version python utiliza?
Python 3.6

## Como se que version python tengo?
* `python -V | python3 -V`


## Como lo utiliso?

Si `fasterjack.py` y sus dependencias estan en Escritorio:
1) Abra terminal, Escriba `cd Escritorio`
2) Ejecute bajo Python 3.6:
* `python3 fasterjack.py -t www.ejemplo.com` 
* `python3 fasterjack.py -h` para acceder al menu de ayuda.

## Opciones de Configuracion

* `-h = Menu de Ayuda`
* `-t = Web o IP`
* `-p = Puerto   --> defecto: 80 Optimo: [80 o 443]`
* `-c = Clientes --> defecto: 50 Optimo: [30-135]`
* `-m = Metodo   --> defecto: RANDOM Opciones: [get o post]`
* `-T = Habilitar el enrutamiento TOR, por defecto: Desactivado`


## Ejemplos de comandos.

  Sin TOR:
* `python fasterjack.py -t www.ejemplo.com`
* `python fasterjack.py -t www.ejemplo.com -p 443 -c 40 -m get`
  Con TOR:
* `python fasterjack.py -t www.ejemplo.com -T`
* `python fasterjack.py -t www.ejemplo.com -p 443 -c 40 -m get -T`

## Como Instalar PYTHON 3.6 ?
## Termux
Seguir instrucciones Linux Sudo y remplazar codigo.
Remplazar: 
* `sudo apt-get`
* `sudo apt-get install`
Por:
* `pkg`
* `pkg install`

## Linux con SUDO

Abrir terminal:
* `sudo apt-get update`
* `sudo apt-get install build-essential checkinstall`
* `sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev`
* `sudo apt-get install python3.6`

## Tengo problemas para instalar PYTHON 3.6
* `sudo apt-get install software-properties-common`
* `sudo add-apt-repository ppa:deadsnakes/ppa`
* `sudo apt-get update`
* `sudo apt-get install build-essential checkinstall`
* `sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev`
* `sudo apt-get install python3.6`

## Revisamos que python esta instalado correctamente
* `python3 -V`

## Como se si tengo Tor Network instalado?
Abrir Terminal:
* `tor --version`

## Como Instalo Tor Network
* `sudo apt-get update`
* `sudo apt-get install tor`
* `sudo apt-get install torsocks`
* `sudo apt-get install tor-geoipdb`
* `sudo /etc/init.d/tor restart`

