def leerLista():
  try:
    archivoTexto=open("listaDePersonajes.txt","r")
    pOnePiece=archivoTexto.read().split("\n")
    print("Se ha encontrado la lista de personajes")
  except FileNotFoundError as noArchivo:
  # Creamos un archivo DEFAULTque contenga los nombres de los personajes almacenados en un string
    print("No se ha podido Encontrar la lista de Personajes, Se cargará la lista de Personajes Por Default")
    archivoTexto=open("listaDePersonajes.txt","w")
    pOnePiece="Monkey D. Luffy\nRoronoa Zoro\nNami\nSanji Vinsmoke\nUsopp\nChopper\nRobin\nFranky\nBrook\nJimbe\nBuggy\nAlvida\nDon Creek\nCaptain Kuro\nArlong\nCocodrile\nEnel\nRob Rucci\nDoflamingo\nBig Mom\nKaido\nDracule Mihawk\nGekko Moriah\nPrincesa Nefertari Vivi\nPortgas D. Ace\nMarshall D.Teach\nAkainu\nShanks\nGol D. Roger\nTrafalgar D. Water Law\nZeff\nEmporio Ivankov\nCamie\nCaribu\nDalton\nInazuma\nLaboon\nPandaman\nNico Olvia\nCrocus\nKaku\nBlueno"
    archivoTexto.write(pOnePiece)
    archivoTexto.close()
    archivoTexto=open("listaDePersonajes.txt","r")
    pOnePiece=archivoTexto.read().split("\n")
  listas=[pOnePiece,]
  return listas;

leerLista()