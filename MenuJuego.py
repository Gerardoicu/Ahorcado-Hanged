from tkinter import *
from Ahorcado import *
from tkinter import messagebox
from tkinter import filedialog
class MenuJuego:
	def __init__(self):
	#VENTANA
		self.root=Tk()
		self.root.title("Ahorcado")
	#FRAME
		self.frame=Frame()
		self.frame.pack()
		self.frame.config(bg="black",width="411", height="300")
		self.root.resizable(0,0)
		#+++++++++++++++++++++++++++++++++++++++++++++ CENTRAR VENTANA AL INICIAR ++++++++++++++++++++++++
		self.windowWidth = self.root.winfo_reqwidth()
		self.windowHeight = self.root.winfo_reqheight()
		#positionRight = int(raiz.winfo_screenwidth()/2 - windowWidth/2)
		#positionDown = int(raiz.winfo_screenheight()/2 - windowHeight/2)
		self.positionRight=100
		self.positionDown=100
		self.root.geometry("+{}+{}".format(self.positionRight,self.positionDown))
		
	# BARRA DEL MENU
		self.barraMenu=Menu(self.root)
		self.root.config(menu=self.barraMenu,background="black")
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

	def getRoot(self):
		return self.root
	def setRoot(self,root):
		self.root=root

	def getFrame(self):
		return self.frame
	def setFrame(self,frame):
		self.frame=frame

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
class Pantalla1(MenuJuego):
	def __init__(self):
	
		super().__init__()
		photo1 =PhotoImage(file="resources/img/boton1.gif")
		button1 =Button(super().getFrame(), compound=TOP,image=photo1, bg='black', command=self.click)
		button1.pack(side=LEFT, padx=2, pady=2)
		button1.image = photo1
		super().getRoot().mainloop()
	def click(self):
		super().getRoot().destroy()
		pantalla2=Pantalla2()			
class Pantalla2(MenuJuego):
	def __init__(self):
		super().__init__()
		label = Label(super().getRoot(), text=self.getEtiqueta(),bg="black",fg="white",font=("Helvetica", 20))
		adivinar=Label(super().getRoot(), text="ADIVINA EL PERSONAJE:",bg="black",fg="white",font=("Helvetica", 20))
		label.pack()
		super().getRoot().mainloop()
	def getEtiqueta(self):
		return "etiqueta ejemplo"	
pantalla=Pantalla2()	

