import json


def cargarDicionario():
	
	pOnePiece=dict()
	pOnePiece={"One Piece":["Monkey D. Luffy","Roronoa Zoro","Nami"]}

	
	return pOnePiece

	
def escribirEnArchivo(diccionario):
	diccionario=dict()
	archivoTexto=open("listaDePersonajes.txt","w")
	archivoTexto.write(str(diccionario))

## debe convertir el contenido de el txt a un diccionario
def leerEnArchivo():
	diccionario=dict()
	archivoTexto=open("listaDePersonajes.txt","r")
	texto=archivoTexto.read()
	texto=texto.replace("\'", "\"")
	diccionario=json.loads(texto)

	return diccionario



def agregarDiccionario(diccionario,key,elementos):
	diccionario.update({key:elementos})
	return diccionario
def eliminarDiccionario(diccionario,key):
	del diccionario[key]
	return diccionario

def agregarNombre(diccionario,key,nombre):
	elementos=list()
	elementos=diccionario[key]
	elementos.append(nombre)
	diccionario.update({key:elementos})
	return diccionario
def eliminarNombre(diccionario,key,nombre):
	elementos=list()
	elementos=diccionario[key]
	if nombre in elementos:
		posicion=elementos.index(nombre)
	elementos.pop(posicion)

	diccionario.update({key:elementos})
	return diccionario

def mostrarNombresListas(diccionario):
	for key, value in diccionario.items() :
		print (key, value)
def mostrarLista(diccionario,key):
	print(key,diccionario[key])
pSeries=dict()
pNaruto=list()
pNaruto=["Naruto","Sasuke","Kakashi"]
pBleach=list()
pBleach=["Ichigo","Rukia","Renji"]
pSeries=cargarDicionario()
pSeries=agregarDiccionario(pSeries,"Bleach",pBleach)
pSeries=agregarDiccionario(pSeries,"Naruto",pNaruto)
pSeries=agregarNombre(pSeries,"Naruto","Rock Lee")
pSeries=eliminarNombre(pSeries,"Naruto","Rock Lee")
escribirEnArchivo(cargarDicionario())
leerEnArchivo()
