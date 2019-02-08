import random
import json
from io import open
class ManipulacionArchivo:

	def cargarDicionario(self):
	  pOnePiece=dict()
	  pOnePiece={"One Piece":["Monkey D. Luffy"," Roronoa Zoro","Nami","Sanji Vinsmoke","Usopp","Chopper","Robin","Franky","Brook","Jimbe","Buggy","Alvida","Don Creek","Captain Kuro","Arlong","Cocodrile","Enel","Rob Rucci","Doflamingo","Big Mom","Kaido","Dracule Mihawk","Gekko Moriah","Princesa Nefertari Vivi","Portgas D. Ace","Marshall D.Teach","Akainu","Shanks","Gol D. Roger","Trafalgar D. Water Law","Zeff","Emporio Ivankov","Camie","Caribu","Dalton","Inazuma","Laboon","Pandaman","Nico Olvia","Crocus","Kaku","Blueno"]}
	  return pOnePiece

	def escribirEnArchivo(self,diccionario):
	  archivoTexto=open("listaDePersonajes.txt","w")
	  archivoTexto.write(str(diccionario))
	  archivoTexto.close()
	  return diccionario

	def leerLista(self):
		  diccionario=dict()
		  try:
		    diccionario=self.leerEnArchivo()
		    print("Se ha encontrado la lista de personajes")
		  except FileNotFoundError as noArchivo:
		  # Creamos un archivo DEFAULTque contenga los nombres de los personajes almacenados en un string
		    print("No se ha podido Encontrar la lista de Personajes, Se cargará la lista de Personajes Por Default")
		    diccionario=escribirEnArchivo( cargarDicionario())         
		  return diccionario
		  
	def leerEnArchivo(self):
	  diccionario=dict()
	  archivoTexto=open("listaDePersonajes.txt","r")
	  texto=archivoTexto.read()
	  texto=texto.replace("\'", "\"")
	  diccionario=json.loads(texto)
	  return diccionario

	def agregarDiccionario(self,diccionario,key,elementos):
	  diccionario.update({key:elementos})
	  self.escribirEnArchivo(diccionario)
	  return diccionario
	def eliminarDiccionario(self,diccionario,key):
	  del diccionario[key]
	  return diccionario

	def agregarNombre(self,diccionario,key,nombre):
	  elementos=list()
	  elementos=diccionario[key]
	  elementos.append(nombre)
	  diccionario.update({key:elementos})
	  self.escribirEnArchivo(diccionario)
	  return diccionario
	def eliminarNombre(self,diccionario,key,nombre):
	  elementos=list()
	  elementos=diccionario[key]
	  if nombre in elementos:
	    posicion=elementos.index(nombre)
	  elementos.pop(posicion)

	  diccionario.update({key:elementos})
	  return diccionario
	def mostrarKeys(self,diccionario):
	  for key in diccionario.keys() :
	    print (key)
	def mostrarNombresListas(self,diccionario):
	  for key, value in diccionario.items() :
	    print (key, value)
	def mostrarLista(self,diccionario,key):
	  print(key,diccionario[key])
	# def agregarLista(diccionario):
	#   listas=list()
	#   archivoTexto=open("listaDePersonajes.txt","r")
	#   diccionarios = json.loads(archivoTexto.read())
	#   for i in range(len(diccionarios)):
	#     listas.append(diccionarios[i])
	#   listas.append(diccionario)
	#   with open("listaDePersonajes.txt", "w") as fout:
	#     json.dump(listas, fout)
	#   return listas## convertir la lista en String
	def agregarPersonaje(self,personaje,personajes):
	  aux=""
	  personajes.append(personaje)
	  for personaje in personajes:
	    aux=aux+personaje+"\n"
	  aux=aux[:-1]
	  archivoTexto=open("listaDePersonajes.txt","w")
	  archivoTexto.write(aux)
	  archivoTexto.close()
	  return aux