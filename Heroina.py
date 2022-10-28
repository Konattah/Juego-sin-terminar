import tkinter as tk

class heroina(object):
	def __init__(self, canvas, ventana):
		self.canvas = canvas
		self.ventana = ventana
		self.imagen_momento = None
		self.TrajeMaga_expresion2 = tk.PhotoImage(file = 'Heroina/TrajeMaga_expresion2.png')
		self.Traje_Cita_Pos1_Ex1 = tk.PhotoImage(file = 'Heroina/Traje_Cita_Pos1_Ex1.png')
		self.Traje_Cita_Pos1_Ex2 = tk.PhotoImage(file = 'Heroina/Traje_Cita_Pos1_Ex2.png')
		self.Traje_Cita_Pos1_Ex4 = tk.PhotoImage(file = 'Heroina/Traje_Cita_Pos1_Ex4.png')
		self.Traje_Cita_Pos1_Ex5 = tk.PhotoImage(file = 'Heroina/Traje_Cita_Pos1_Ex5.png')
		self.Traje_Cita_Pos1_Ex8 = tk.PhotoImage(file = 'Heroina/Traje_Cita_Pos1_Ex8.png')
		self.Traje_Cita_Pos1_Ex13 = tk.PhotoImage(file = 'Heroina/Traje_Cita_Pos1_Ex13.png')
		self.Traje_Cita_Pos1_Ex18 = tk.PhotoImage(file = 'Heroina/Traje_Cita_Pos1_Ex18.png')
		self.Traje_Cita_Pos2_Ex3 = tk.PhotoImage(file = 'Heroina/Traje_Cita_Pos2_Ex3.png')

	def quitar_heroina(self):
		self.canvas.delete(self.imagen_momento)

	def heroina_menu_principal(self):
		self.imagen_momento = self.canvas.create_image(640, 435, image = self.TrajeMaga_expresion2)

	def img_Traje_Cita_Pos1_Ex1(self):
		self.imagen_momento = self.canvas.create_image(640, 435, image = self.Traje_Cita_Pos1_Ex1)

	def img_Traje_Cita_Pos1_Ex2(self):
		self.imagen_momento = self.canvas.create_image(640, 435, image = self.Traje_Cita_Pos1_Ex2)

	def img_Traje_Cita_Pos1_Ex4(self):
		self.imagen_momento = self.canvas.create_image(640, 435, image = self.Traje_Cita_Pos1_Ex4)

	def img_Traje_Cita_Pos1_Ex5(self):
		self.imagen_momento = self.canvas.create_image(640, 435, image = self.Traje_Cita_Pos1_Ex5)

	def img_Traje_Cita_Pos1_Ex8(self):
		self.imagen_momento = self.canvas.create_image(640, 435, image = self.Traje_Cita_Pos1_Ex8)

	def img_Traje_Cita_Pos1_Ex13(self):
		self.imagen_momento = self.canvas.create_image(640, 435, image = self.Traje_Cita_Pos1_Ex13)

	def img_Traje_Cita_Pos1_Ex18(self):
		self.imagen_momento = self.canvas.create_image(640, 435, image = self.Traje_Cita_Pos1_Ex18)

	def img_Traje_Cita_Pos2_Ex3(self):
		self.imagen_momento = self.canvas.create_image(640, 435, image = self.Traje_Cita_Pos2_Ex3)