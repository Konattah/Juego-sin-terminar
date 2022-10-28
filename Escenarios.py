import tkinter as tk

class escenarios(object):
	def __init__(self, ventana, canvas):
		self.canvas = canvas
		self.ventana = ventana
		self.MenuPrincipalIMG = tk.PhotoImage(file = 'MenuPrincipal.png')
		self.cuadro_texto = tk.PhotoImage(file = 'textbox.png')
		self.img_cuadro_texto = None
		self.fondo01 = tk.PhotoImage(file = 'Fondos/01.png')
		self.fondo02 = tk.PhotoImage(file = 'Fondos/02.png')
		self.fondo03 = tk.PhotoImage(file = 'Fondos/03.png')
		self.fondo04 = tk.PhotoImage(file = 'Fondos/04.png')
		self.fondo05 = tk.PhotoImage(file = 'Fondos/05.png')
		self.fondo06 = tk.PhotoImage(file = 'Fondos/06.png')
		self.fondo07 = tk.PhotoImage(file = 'Fondos/07.png')
		self.fondo08 = tk.PhotoImage(file = 'Fondos/08.png')
		self.fondo09 = tk.PhotoImage(file = 'Fondos/09.png')
		self.fondo10 = tk.PhotoImage(file = 'Fondos/10.png')
		self.fondo11 = tk.PhotoImage(file = 'Fondos/11.png')
		self.fondo12 = tk.PhotoImage(file = 'Fondos/12.png')
		self.fondo13 = tk.PhotoImage(file = 'Fondos/13.png')
		self.fondo14 = tk.PhotoImage(file = 'Fondos/14.png')
		self.fondo15 = tk.PhotoImage(file = 'Fondos/15.png')
		self.fondo16 = tk.PhotoImage(file = 'Fondos/16.png')
		self.fondo17 = tk.PhotoImage(file = 'Fondos/17.png')
		self.fondo18 = tk.PhotoImage(file = 'Fondos/18.png')
		self.fondo19 = tk.PhotoImage(file = 'Fondos/19.png')
		self.fondo20 = tk.PhotoImage(file = 'Fondos/20.png')

	def menu_Principal(self):
		self.canvas.create_image(640, 360, image = self.MenuPrincipalIMG)

	def mostrar_cuadro_texto(self):
		self.img_cuadro_texto = self.canvas.create_image(640, 600, image = self.cuadro_texto)

	def sacar_cuadro_texto(self):
		self.canvas.delete(self.img_cuadro_texto)

	def img_fondo09(self):
		self.canvas.destroy()
		self.canvas = tk.Canvas(self.ventana, width = 1280, height = 720)
		self.canvas.pack()
		self.canvas.create_image(640, 360, image = self.fondo09)

	def img_fondo20(self):
		self.canvas.destroy()
		self.canvas = tk.Canvas(self.ventana, width = 1280, height = 720)
		self.canvas.pack()
		self.canvas.create_image(640, 360, image = self.fondo20)