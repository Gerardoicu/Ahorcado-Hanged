from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
class MenuJuego:

	def __init__(self):
		self.root=Tk()
		self.root.title("Ahorcado")
		self.root.resizable(0,0);
		# creamos la barra menu y le decimos que va a ir dentro de la ventana
		self.barraMenu=Menu(self.root)
	def infoAdicional(self):
		messagebox.showinfo("Procesador de Gerardo"," Procesador de Textos 2018")
		
	def avisoLicencia(self):
		messagebox.showwarning("Licencia", "El producto no ha sido activado")
	
	def salirAplicacio(self):
		#valor=messagebox.askquestion("Salir", "Deseas salir de la aplicacion?")
		valor=messagebox.askokcancel("Salir", "Deseas salir de la aplicacion?")
		if valor==True:
			self.root.destroy()
	def cerrarDocumento(self):
		valor=messagebox.askretrycancel("Reintentar", "No es posible cerrar, documento bloqueado")
		if valor==False:
			self.root.destroy()
	def abrirDocumento(self):
		fichero=filedialog.askopenfilename(title="Abrir",initialdir="C://",filetypes=(("Ficheros de Excel","*.xlsx"),("Ficheros de Texto","*.txt"),("Todos los ficheros","*.*")))
		print(fichero)
	def menu(self):
	
		# tenemos que ademas agregar el elemento menu en los parametros config
		self.root.config(menu=self.barraMenu,width=300, height=300)
		
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
		self.root.mainloop()
