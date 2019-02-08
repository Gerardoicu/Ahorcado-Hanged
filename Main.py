
from Ahorcado import Ahorcado
from ManipulacionArchivo import ManipulacionArchivo

class Main:
  #VARIABLES GLOBALES
  def main():
    obj= ManipulacionArchivo()
    ahorcado=Ahorcado()
    opcion=True;
    index="One Piece"
    while opcion==True: 
      listas=obj.leerLista()  
      print("###################################################")
      print("MENU DE OPCIONES")
      print("0 >>>>> Jugar")
      print("1 >>>>> Agregar Personajes")
      #INCOMPLETO
      print("2 >>>>> Crear una lista Nueva de Personajes")
      #INCOMPLETO
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
Main.main()

     


  




