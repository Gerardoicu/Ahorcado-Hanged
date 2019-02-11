from tkinter import *

from Ahorcado import *
from ManipulacionArchivo import ManipulacionArchivo
from tkinter import messagebox
from tkinter import filedialog

class MenuJuego(Tk):
	def __init__(self):
	#VENTANA	
		super().__init__()
		self.title("Ahorcado")
	#FRAME

		#self.root.geometry('411x300')
	
		#+++++++++++++++++++++++++++++++++++++++++++++ CENTRAR VENTANA AL INICIAR ++++++++++++++++++++++++
		self.windowWidth = self.winfo_reqwidth()
		self.windowHeight = self.winfo_reqheight()
		#positionRight = int(raiz.winfo_screenwidth()/2 - windowWidth/2)
		#positionDown = int(raiz.winfo_screenheight()/2 - windowHeight/2)
		self.positionRight=100
		self.positionDown=100
		self.geometry("+{}+{}".format(self.positionRight,self.positionDown))
		
	# BARRA DEL MENU
		self.barraMenu=Menu(self)
		self.config(menu=self.barraMenu,background="black")
		self.archivoJugar=Menu(self.barraMenu, tearoff=0)
		self.archivoJugar.add_command(label="Jugar",command=self.abrirDocumento)
		self.archivoJugar.add_separator()
		self.archivoJugar.add_command(label="Cerrar",command=self.salirAplicacio)
		MenuAgregar=Menu(self.barraMenu, tearoff=0)
		MenuAgregar.add_command(label="Serie")
		MenuAgregar.add_command(label="Personaje")
		archivoHerramientas=Menu(self.barraMenu, tearoff=0)
		archivoAyuda=Menu(self.barraMenu, tearoff=0)
		archivoAyuda.add_command(label="Licencia",command=self.avisoLicencia)
		archivoAyuda.add_command(label="Acerca de..." ,command=self.infoAdicional)
		self.barraMenu.add_cascade(label="Jugar",menu=self.archivoJugar)
		self.barraMenu.add_cascade(label="Agregar...",menu=MenuAgregar)
		self.barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)

	def getFrame(self):
		return self.frame
	def infoAdicional(self):
		messagebox.showinfo("Procesador de Gerardo"," Procesador de Textos 2018")
		
	def avisoLicencia(self):
		messagebox.showwarning("Licencia", "El producto no ha sido activado")
	
	def salirAplicacio(self):
		#valor=messagebox.askquestion("Salir", "Deseas salir de la aplicacion?")
		valor=messagebox.askokcancel("Salir", "Deseas salir de la aplicacion?")
		if valor==True:
			self.destroy()
	def cerrarDocumento(self):
		valor=messagebox.askretrycancel("Reintentar", "No es posible cerrar, documento bloqueado")
		if valor==False:
			self.destroy()
	def abrirDocumento(self):
		fichero=filedialog.askopenfilename(title="Abrir",initialdir="C://",filetypes=(("Ficheros de Excel","*.xlsx"),("Ficheros de Texto","*.txt"),("Todos los ficheros","*.*")))
		print(fichero)
class Pantalla1(Toplevel):
	def __init__(self):
		pass
	
	
class Pantalla2(Toplevel):
	def __init__(self):
		super().__init__()
		########

		##########

class Pantalla3(Toplevel):
	def __init__(self):
		super().__init__()


	
class Pantalla4(Toplevel):
	def __init__(self):
		super().__init__()
		
class MyFrame(Frame):
	def __init__(self,parent):
	
		super().__init__()
		self.click=False
		self.photo1 =PhotoImage(file="resources/img/boton1.gif")
		self.button1 =Button(parent,compound=TOP,image=self.photo1, bg='black', command=self.getClick)
		self.button1.pack(side=LEFT, padx=2, pady=2)
		self.button1.image = self.photo1			 
	def getClick(self):
		pass			

pantalla= MenuJuego()
frame1=MyFrame(pantalla)
pantalla.mainloop()


