#!/usr/bin/python
# -*- coding: latin-1 -*-
# 
# Este es el programa server de un servicio de echo. Un servicio de echo (eco)
# como su nombre lo sugiere quiere decir que lo que recibe el servidor lo 
# regresa tal cual al cliente. Si el cliente envia un 'hola mundo' el servidor
# le regresara un 'hola mundo'.
#
# En este programa el cliente digitara una cadena se la enviara al servidor
# y este enviara la cadena de vuelta en pedazos de 16 bytes.
#
# Complete el programa en aquellas lineas que dice # tu codigo aqui
# Este servidor tiene como proposito escuchar a un cliente y enviarle de 
# regreso los datos por este enviados
#

import socket 
import sys
import argparse

host = ''
data_payload = 2048
backlog = 5 # valor que recibe la funcion socket.listen()

def echo_server(port): 
	# Cree un socket IPv4 y de tipo TCP
	# tu codigo aqui
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Que el puerto de red del socket se pueda reutilizar
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_address = (host, port)
	print "Starting up echo server on %s port %s"%server_address
	# Asocie el socket s al server_address
	# tu codigo aqui. Hint: use el metodo bind()
	s.bind (server_address)

	# Ahora escuche por clientes, use la variable backlog
	# tu codigo aqui. Hint: use el metodo listen()
	s.listen (backlog)

	while True: # Esperando por conexiones de los clientes
		print "Esperando por mensajes de clientes"
		client, address = s.accept() # espera bloqueante por cliente
		# leer datos de una longitud maxima dada por la variable 
		# data_payload
		# tu codigo aqui
		data = s.recv(data_payload)

		if data:
			print "Data: %s"%data
			# enviele los mismos datos al cliente
			# tu codigo aqui. Hint: Use el metodo send
			s.send(data)

			print "send %s bytes back to %s"%(data,address)
		# cierre conexion con el cliente
		# tu codigo aqui. Hint: Use el metodo close()
		s.close()


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'Socket Server Example')
	parser.add_argument('--port', action = 'store', dest = 'port', type = int, required = True)
	given_args = parser.parse_args()
	port = given_args.port
	echo_server(port)
