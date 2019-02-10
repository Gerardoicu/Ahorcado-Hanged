
from Musica import Musica
from Ahorcado import Ahorcado
from ManipulacionArchivo import ManipulacionArchivo
from tkinter import *
import logging

class Main:
  #VARIABLES GLOBALES
  #Crear una clase de la que hereden el constructor todas las demas ventanas
  #pantalla 2
  #volumen
  #pantalla 4
  #pantalla 5
  #pantalla 6
  #pantalla 3
  #base de datos

	def main():
		Musica().play_sound()
	
		logging.warning('is when this event was logged.')
		
		pantalla1=Pantalla1()
	def consola():
		opcion=True;
		index="One Piece"
		ahorcado=Ahorcado()
		obj= ManipulacionArchivo()
		while opcion==True: 
			listas=obj.leerLista()  
			print("###################################################")
			print("MENU DE OPCIONES")
			print("0 >>>>> Jugar")
			print("1 >>>>> Agregar Personajes")
			print("2 >>>>> Crear una lista Nueva de Personajes")
			print("3 >>>>> Cambiar Lista Actual De Personajes")
			print("4 >>>>> Ver Todas las listas")
			print("5 >>>>> Salir")
			opcionLeer=input();
			if opcionLeer=="0":
				ahorcado.juego(listas[index])
				print("Fin de el juego")
			elif opcionLeer=="1":
				print("Esta es la lista De personajes actualmente:")
				print(listas[index])
				personajeNuevo= input("Dame el nombre de el personaje que deseas agregar :")
				#Debe permitir Espacios y puntos
				if re.search('^([\dA-ZÑÁÉÍÓÚa-zñáéíóú]+[-]?[\.]?[\s]?)+$',personajeNuevo):
					listas=obj.agregarNombre(listas,index,personajeNuevo)
					print(listas[index])
					print("Se ha agregado un personaje nuevo")
				else:
					print("No es un Carácter Válido") 
			elif opcionLeer=="2":
				nombres=list()
				serie=input("Por Favor Escribe el nombre de la serie, programa o tema que quieras guardar")
				while True:
					listaN=input("Por favor escribe el nombre de el Personaje")
		          ###### agregar un lista que guarde los nombres de las lista (PENDIENTES)
					nombres.append(listaN)
					opcionsalir=input("Deseas agregar otro elemento a la lista? s/n")
					if opcionsalir=="n" or opcionsalir=="no":
						break
				listas=obj.agregarDiccionario(listas,serie,nombres)
				print("Lista agregada Con exito!")
			elif opcionLeer=="3":
				print("Estas son las listas actualmente guardadas")
				obj.mostrarKeys(listas)
				index=input("Por favor escribe el nombre de una de las listas guardadas:")
			elif opcionLeer=="4":
				print("Estas son las listas actualmente guardadas")
				obj.mostrarNombresListas(listas)  
			elif opcionLeer=="5":
				break
			elif opcion!="5" and opcion!="4" and opcion!="3" and  opcion!="2" and opcion!="1" and opcion!="0":
				print("No es una opcion Valida")   

Main.consola()
     
