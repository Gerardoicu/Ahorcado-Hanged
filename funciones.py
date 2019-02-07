import random
import re
import json
from io import open


def cargarDicionario():
  pOnePiece=dict()
  pOnePiece={"One Piece":["Monkey D. Luffy"," Roronoa Zoro","Nami","Sanji Vinsmoke","Usopp","Chopper","Robin","Franky","Brook","Jimbe","Buggy","Alvida","Don Creek","Captain Kuro","Arlong","Cocodrile","Enel","Rob Rucci","Doflamingo","Big Mom","Kaido","Dracule Mihawk","Gekko Moriah","Princesa Nefertari Vivi","Portgas D. Ace","Marshall D.Teach","Akainu","Shanks","Gol D. Roger","Trafalgar D. Water Law","Zeff","Emporio Ivankov","Camie","Caribu","Dalton","Inazuma","Laboon","Pandaman","Nico Olvia","Crocus","Kaku","Blueno"]}
  return pOnePiece

  
def escribirEnArchivo(diccionario):
  archivoTexto=open("listaDePersonajes.txt","w")
  archivoTexto.write(str(diccionario))
  archivoTexto.close()
  return diccionario
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
  escribirEnArchivo(diccionario)
  return diccionario
def eliminarDiccionario(diccionario,key):
  del diccionario[key]
  return diccionario

def agregarNombre(diccionario,key,nombre):
  elementos=list()
  elementos=diccionario[key]
  elementos.append(nombre)
  diccionario.update({key:elementos})
  escribirEnArchivo(diccionario)
  return diccionario
def eliminarNombre(diccionario,key,nombre):
  elementos=list()
  elementos=diccionario[key]
  if nombre in elementos:
    posicion=elementos.index(nombre)
  elementos.pop(posicion)

  diccionario.update({key:elementos})
  return diccionario
def mostrarKeys(diccionario):
  for key in diccionario.keys() :
    print (key)
def mostrarNombresListas(diccionario):
  for key, value in diccionario.items() :
    print (key, value)
def mostrarLista(diccionario,key):
  print(key,diccionario[key])
def agregarLista(diccionario):
  listas=list()
  archivoTexto=open("listaDePersonajes.txt","r")
  diccionarios = json.loads(archivoTexto.read())
  for i in range(len(diccionarios)):
    listas.append(diccionarios[i])
  listas.append(diccionario)
  with open("listaDePersonajes.txt", "w") as fout:
    json.dump(listas, fout)
  return listas
def leerLista():
  diccionario=dict()
  try:
    diccionario=leerEnArchivo()
    print("Se ha encontrado la lista de personajes")
  except FileNotFoundError as noArchivo:
  # Creamos un archivo DEFAULTque contenga los nombres de los personajes almacenados en un string
    print("No se ha podido Encontrar la lista de Personajes, Se cargará la lista de Personajes Por Default")
    diccionario=escribirEnArchivo( cargarDicionario())         
  return diccionario;
## convertir la lista en String
def agregarPersonaje(personaje,personajes):
  aux=""
  personajes.append(personaje)
  for personaje in personajes:
    aux=aux+personaje+"\n"
  aux=aux[:-1]
  archivoTexto=open("listaDePersonajes.txt","w")
  archivoTexto.write(aux)
  archivoTexto.close()
  return aux

def pintarLineas(lineas):
  palabraSecreta=""
  for i in lineas:
    if i==" ":
      palabraSecreta=palabraSecreta+" "
    elif i==".":
      palabraSecreta=palabraSecreta+"."
    else:
      palabraSecreta=palabraSecreta+"_"
   
  return(palabraSecreta)
def letrasEncontradas(adivinar):
  count= len(adivinar)-(adivinar.count("_")+adivinar.count(".")+adivinar.count(" "))
  return count
def obtenerPersonajeAlzar(pOnePiece):
    indice= random.randint(0,len(pOnePiece)-1)
    return pOnePiece[indice]
def separarCorrectaseIncorrectas(letra,adivinar,letrasCorrectas,letrasIncorrectas):
  for i in letra:
    if not i in adivinar and not i in letrasIncorrectas:
      letrasIncorrectas=letrasIncorrectas+i
    if i in adivinar and not i in letrasCorrectas:
      letrasCorrectas=letrasCorrectas+i
  lista=letrasCorrectas,letrasIncorrectas
  return lista
def checarExistencia(letras,adivinar):
    validar=False
    for i in letras:
      if i in adivinar:
        validar=True
        break;
    return validar
def acomodarLetras(adivinar,letras):
  lineas=len(adivinar)*"_"

  for j in letras:
    for i in  range(len(adivinar)): 
      if j==adivinar[i]:
        lineas=lineas[:i]+lineas[i].replace("_",j)+lineas[i+1:] 
  return lineas
def pintarEspacios(lineas):
  aux=""
  for i in lineas:
    aux=aux+i+" "
  return aux

def menu(contador,letrasCorrectas,letrasIncorrectas,palabraOculta,letra):
  print("Letras acertadas: ",len(letrasCorrectas)-2," (",letrasCorrectas[2:],")")
  print("Coincidencias: ", letrasEncontradas(palabraOculta))
  print("Letras NO acertadas: ",len(letrasIncorrectas)," (",letrasIncorrectas,")")
  if len(letrasIncorrectas)==1:
    print("Pierdes",len(letrasIncorrectas)," oportunidad")
  elif len(letrasIncorrectas)>2:
    print("Pierdes",len(letrasIncorrectas)," oportunidades")
    print("Número de intentos restantes : ",6-len(letrasIncorrectas))
  elif len(letrasIncorrectas)>=6:
    print("Ya no te quedan más oportunidades")
    print("Número de intentos restantes : ",0)
  else:
    print("Número de intentos restantes: ",6-len(letrasIncorrectas));
  print("Adivina el Personaje: ",end="")
  print(pintarEspacios(palabraOculta.capitalize()))
  print(IMAGENES_AHORCADO[contador])
def juego(pOnePiece):
  letra=""
  contador=0
  letrasIncorrectas=""
  letrasCorrectas=". "
  adivinar=obtenerPersonajeAlzar(pOnePiece).lower()
  palabraOculta=pintarLineas(adivinar)
  print("Comienza el juego de el ahorcado: ")
  while True:
    if palabraOculta==adivinar:
      print("######################################################################################")
      print("FELICIDADES! haz ganado el juego, el personaje es:", adivinar.title() )
      print("######################################################################################")
      menu(contador,letrasCorrectas,letrasIncorrectas,palabraOculta,letra)
      break
    if contador>=6:
      print("haz perdido!")
      menu(contador,letrasCorrectas,letrasIncorrectas,palabraOculta,letra)
      print("El personaje era: ",pintarEspacios(adivinar.title()))
      break
    menu(contador,letrasCorrectas,letrasIncorrectas,palabraOculta,letra)
    if len(letrasCorrectas)!=2 or len(letrasIncorrectas)!=0:
      letra=input("Escribe otra letra o palabra:").lower()
    else:
      letra=input("Escribe una letra o palabra:").lower() 
    if letra in letrasCorrectas or letra in letrasIncorrectas:
      print("usted ya ha elegido esa letra ")
    elif checarExistencia(letra,adivinar)==True: 
      letrasCorrectas= separarCorrectaseIncorrectas(letra,adivinar,letrasCorrectas,letrasIncorrectas)[0]
      letrasIncorrectas=separarCorrectaseIncorrectas(letra,adivinar,letrasCorrectas,letrasIncorrectas)[1]
      if len(letrasIncorrectas)>=6:
        contador=6;
      else:
        print("Haz acertado!")
        palabraOculta= acomodarLetras(adivinar,letrasCorrectas)
        contador=len(letrasIncorrectas)
    elif checarExistencia(letra,adivinar)==False:
      print(" No has descubierto ninguna letra!")
      letrasCorrectas= separarCorrectaseIncorrectas(letra,adivinar,letrasCorrectas,letrasIncorrectas)[0]
      letrasIncorrectas=separarCorrectaseIncorrectas(letra,adivinar,letrasCorrectas,letrasIncorrectas)[1]
      contador=len(letrasIncorrectas)
      if contador>6:
        contador=6
  

IMAGENES_AHORCADO = ['''
     +---+
     |   |
         |
         |
         |
         |
  =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |

  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']
