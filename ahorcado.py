import random
class Ahorcado:
	def pintarLineas(self,lineas):
	  palabraSecreta=""
	  for i in lineas:
	    if i==" ":
	      palabraSecreta=palabraSecreta+"  "
	    elif i==".":
	      palabraSecreta=palabraSecreta+". "
	    else:
	      palabraSecreta=palabraSecreta+"_ "
	   
	  return(palabraSecreta)
	def letrasEncontradas(self,adivinar):
	  count= len(adivinar)-(adivinar.count("_")+adivinar.count(".")+adivinar.count(" "))
	  return count
	def obtenerPersonajeAlzar(self,pOnePiece):
	    indice= random.randint(0,len(pOnePiece)-1)
	    return pOnePiece[indice]
	def separarCorrectaseIncorrectas(self,letra,adivinar,letrasCorrectas,letrasIncorrectas):
	  for i in letra:
	    if not i in adivinar and not i in letrasIncorrectas:
	      letrasIncorrectas=letrasIncorrectas+i
	    if i in adivinar and not i in letrasCorrectas:
	      letrasCorrectas=letrasCorrectas+i
	  lista=letrasCorrectas,letrasIncorrectas
	  return lista
	def checarExistencia(self,letras,adivinar):
	    validar=False
	    for i in letras:
	      if i in adivinar:
	        validar=True
	        break;
	    return validar
	def acomodarLetras(self,adivinar,letras):
	  lineas=len(adivinar)*"_"

	  for j in letras:
	    for i in  range(len(adivinar)): 
	      if j==adivinar[i]:
	        lineas=lineas[:i]+lineas[i].replace("_",j)+lineas[i+1:] 
	  return lineas
	def pintarEspacios(self,lineas):
	  aux=""
	  for i in lineas:
	    aux=aux+i+" "
	  return aux

	def menu(self,contador,letrasCorrectas,letrasIncorrectas,palabraOculta,letra):
	  print("Letras acertadas: ",len(letrasCorrectas)-2," (",letrasCorrectas[2:],")")
	  print("Coincidencias: ",self.letrasEncontradas(palabraOculta))
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
	  print(self.pintarEspacios(palabraOculta.capitalize()))
	  self.imagenAhorcado(contador)
	
	def juego(self,pOnePiece):
	  letra=""
	  contador=0
	  letrasIncorrectas=""
	  letrasCorrectas=". "
	  adivinar=self.obtenerPersonajeAlzar(pOnePiece).lower()
	  palabraOculta=self.pintarLineas(adivinar)
	  print("Comienza el juego de el ahorcado: ")
	  while True:
	    if palabraOculta==adivinar:
	      print("######################################################################################")
	      print("FELICIDADES! haz ganado el juego, el personaje es:", adivinar.title() )
	      print("######################################################################################")
	      self.menu(contador,letrasCorrectas,letrasIncorrectas,palabraOculta,letra)
	      break
	    if contador>=6:
	      print("haz perdido!")
	      self.menu(contador,letrasCorrectas,letrasIncorrectas,palabraOculta,letra)
	      print("El personaje era: ",self.pintarEspacios(adivinar.title()))
	      break
	    self.menu(contador,letrasCorrectas,letrasIncorrectas,palabraOculta,letra)
	    if len(letrasCorrectas)!=2 or len(letrasIncorrectas)!=0:
	      letra=input("Escribe otra letra o palabra:").lower()
	    else:
	      letra=input("Escribe una letra o palabra:").lower() 
	    if letra in letrasCorrectas or letra in letrasIncorrectas:
	      print("usted ya ha elegido esa letra ")
	    elif self.checarExistencia(letra,adivinar)==True: 
	      letrasCorrectas=self.separarCorrectaseIncorrectas(letra,adivinar,letrasCorrectas,letrasIncorrectas)[0]
	      letrasIncorrectas=self.separarCorrectaseIncorrectas(letra,adivinar,letrasCorrectas,letrasIncorrectas)[1]
	      if len(letrasIncorrectas)>=6:
	        contador=6;
	      else:
	        print("Haz acertado!")
	        palabraOculta=self.acomodarLetras(adivinar,letrasCorrectas)
	        contador=len(letrasIncorrectas)
	    elif self.checarExistencia(letra,adivinar)==False:
	      print(" No has descubierto ninguna letra!")
	      letrasCorrectas= self.separarCorrectaseIncorrectas(letra,adivinar,letrasCorrectas,letrasIncorrectas)[0]
	      letrasIncorrectas=self.separarCorrectaseIncorrectas(letra,adivinar,letrasCorrectas,letrasIncorrectas)[1]
	      contador=len(letrasIncorrectas)
	      if contador>6:
	        contador=6
	def imagenAhorcado(self,contador):
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
		print(IMAGENES_AHORCADO[contador])	  

