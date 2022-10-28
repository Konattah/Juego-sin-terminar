import tkinter as tk
from Escenarios import *
import tkinter.messagebox
from Heroina import *

class demo(escenarios, heroina):
	def __init__(self, ventana, canvas):
		escenarios.__init__(self, ventana, canvas)
		heroina.__init__(self, canvas, ventana)
		self.siguiente = tk.PhotoImage(file = 'siguiente.png')
		self.anterior = tk.PhotoImage(file = 'anterior.png')
		self.nombre_prota = None
		self.nombre_heroina = 'Hana'
		self.mensaje = None
		self.nombre_personaje = None

	def poner_nombre(self, nombre):
		self.nombre_personaje = self.canvas.create_text(170, 500, text = nombre, font = ('fangsong ti', 25), fill = 'black')

	# Quita el nombre del texbox junto con le mensaje que esté en ella
	def quitar_nombre_mensaje(self):
		self.canvas.delete(self.nombre_personaje)
		self.canvas.delete(self.mensaje)

	# Crea dos archivos de te texto para el guardado de la partida
	def guardar(self, lugar):
		partida = open('guardado/nombre.txt', 'w+')
		partida.write(self.nombre_prota)
		partida.close()

		partida = open('guardado/lugar.txt', 'w+')
		partida.write(lugar)
		partida.close()

	# Guarda el nombre, para el guardado de la partida
	def cargar(self, nombre):
		self.nombre_prota = nombre

	# Lo que se mostrará al pulsar el botón de nuevo juego
	def nuevo_juego(self):
		self.canvas.destroy()
		self.canvas = tk.Canvas(self.ventana, width = 1280, height = 720, bg = 'black')
		self.canvas.pack()
		texto = "Esta es una Demo, por lo tanto, posee solo una ruta con una sola heroina."
		escenarios.mostrar_cuadro_texto(self)
		# gothic; terminal; courier; fangsong ti
		self.canvas.create_text(640, 600, text = texto, font = ('terminal', 20), fill = 'white')
		# Botón
		b_siguiente = tk.Button(self.ventana, image = self.siguiente, command = lambda: (demo.presentacion_prota(self), b_siguiente.destroy()))
		b_siguiente.place(x = 1155, y = 635)
		# Fin Botón

	# Se introducirá el nombre del protagonista en este metodo
	def presentacion_prota(self):
		escenarios.img_fondo20(self)
		escenarios.mostrar_cuadro_texto(self)
		nombre_prota_variable = tk.StringVar()
		ingreso_nombre_prota = tk.Entry(self.canvas, textvariable = nombre_prota_variable, bg = 'grey', font = ('fangsong ti', 15))
		ingreso_nombre_prota.place(x = 300, y = 590)
		self.mensaje = self.canvas.create_text(200, 600, text = 'Ingrese su nombre: ', font = ('terminal', 20), fill = 'white')
		# Boton
		b_siguiente = tk.Button(self.ventana, image = self.siguiente, command = lambda: (demo.comprobacion_nombre(self,ingreso_nombre_prota.get(), ingreso_nombre_prota, b_siguiente)))
		b_siguiente.place(x = 1155, y = 635)
		# Fin boton

	# Comprobación de que el nombre cumpla ciertos parametros
	def comprobacion_nombre(self, nombre, ingreso_nombre_prota, b_siguiente):
		if(len(nombre) == 0):
			tkinter.messagebox.showinfo('Nombre invalido','No se escribió ningún nombre.')
		elif(nombre[0] == ' '):
			tkinter.messagebox.showinfo('Nombre invalido','Primer caracter vacio.')
		elif(len(nombre) > 7):
			tkinter.messagebox.showinfo('Nombre invalido','Puede tener hasta un máximo de 7 caracteres.')
		else:
			b_siguiente.destroy()
			ingreso_nombre_prota.destroy()
			demo.quitar_nombre_mensaje(self)
			self.nombre_prota =  nombre
			demo.palabras_propias(self)

	# Me gusta poner cosas innecesarias XD
	def palabras_propias(self):
		demo.poner_nombre(self, self.nombre_prota)
		##
		texto = 'Soy ' + str(self.nombre_prota) + ' y esta es la historia de mi primera cita, con mi primer amor.'
		self.mensaje = self.canvas.create_text(620, 600, text = texto, font = ('fangsong ti', 17), fill = 'white')
		# Botones
		b_siguiente = tk.Button(self.ventana, image = self.siguiente, command = lambda: (demo.inicio(self), b_siguiente.destroy()))
		b_siguiente.place(x = 1155, y = 635)
		# Fin Botones

	def inicio(self):
		escenarios.img_fondo09(self)
		escenarios.mostrar_cuadro_texto(self)
		# Botones
		b_anterior = tk.Button(self.ventana, image = self.anterior, command = lambda: (escenarios.img_fondo20(self), escenarios.mostrar_cuadro_texto(self), demo.palabras_propias(self), b_siguiente.destroy(), b_anterior.destroy()))
		b_anterior.place(x = 1100, y = 635)
		b_siguiente = tk.Button(self.ventana, image = self.siguiente, command = lambda: (demo.inicio_1(self), b_siguiente.destroy(), b_anterior.destroy()))
		b_siguiente.place(x = 1155, y = 635)
		# Fin Botones
		demo.poner_nombre(self, self.nombre_prota)
		##
		texto = '*Han pasado ya varios meses desde que me siento de esta manera hacia Hana y recientemente pude\nreunir el valor suficiente para poder invitarla a salir.\n\nSiento miedo a que pueda ser rechazado... Pero, lo intentaré.*'
		self.mensaje = self.canvas.create_text(660, 600, text = texto, font = ('fangsong ti', 14), fill = 'white')

	def inicio_1(self):
		self.canvas.delete(self.mensaje)
		texto = 'Vaya... ¿Habré llegado demasiado temprano?'
		self.mensaje = self.canvas.create_text(660, 600, text = texto, font = ('fangsong ti', 14), fill = 'white')
		# Botones
		b_anterior = tk.Button(self.ventana, image = self.anterior, command = lambda: (demo.inicio(self), b_siguiente.destroy(), b_anterior.destroy()))
		b_anterior.place(x = 1100, y = 635)
		b_siguiente = tk.Button(self.ventana, image = self.siguiente, command = lambda: (demo.parte1(self), b_siguiente.destroy(), b_anterior.destroy()))
		b_siguiente.place(x = 1155, y = 635)
		# Fin Botones

	def parte1(self):
		heroina.img_Traje_Cita_Pos1_Ex1(self)
		escenarios.sacar_cuadro_texto(self)
		escenarios.mostrar_cuadro_texto(self)
		demo.quitar_nombre_mensaje(self)
		demo.poner_nombre(self, 'Hana')
		##
		texto = '¡Oh, ' + str(self.nombre_prota) + '!'
		self.mensaje = self.canvas.create_text(660, 600, text = texto, font = ('fangsong ti', 14), fill = 'white')
		# Botones
		b_anterior = tk.Button(self.ventana, image = self.anterior, command = lambda: (heroina.quitar_heroina(self),demo.inicio_1(self), b_siguiente.destroy(), b_anterior.destroy()))
		b_anterior.place(x = 1100, y = 635)
		b_siguiente = tk.Button(self.ventana, image = self.siguiente, command = lambda: (heroina.quitar_heroina(self), demo.parte1_1(self), b_siguiente.destroy(), b_anterior.destroy()))
		b_siguiente.place(x = 1155, y = 635)
		# Fin Botones

	def parte1_1(self):
		heroina.img_Traje_Cita_Pos1_Ex2(self)
		escenarios.sacar_cuadro_texto(self)
		escenarios.mostrar_cuadro_texto(self)
		demo.quitar_nombre_mensaje(self)
		demo.poner_nombre(self, 'Hana')
		##
		texto = 'Eres muy puntual jajaja'
		self.mensaje = self.canvas.create_text(660, 600, text = texto, font = ('fangsong ti', 14), fill = 'white')
		# Botones
		b_anterior = tk.Button(self.ventana, image = self.anterior, command = lambda: (heroina.quitar_heroina(self),demo.parte1(self), b_siguiente.destroy(), b_anterior.destroy()))
		b_anterior.place(x = 1100, y = 635)
		b_siguiente = tk.Button(self.ventana, image = self.siguiente, command = lambda: (demo.decision1(self), b_siguiente.destroy(), b_anterior.destroy()))
		b_siguiente.place(x = 1155, y = 635)
		# Fin Botones

	# Inicio Decision
	def decision1(self):
		escenarios.sacar_cuadro_texto(self)
		demo.quitar_nombre_mensaje(self)
		opcion_A = tk.Button(self.canvas, text = 'Si, me gusta que todo salga perfecto, siempre de acuerdo a lo planeado.', font = ('terminal', 15), width = 93, height = 2, bg = 'blue', fg = 'white', command = lambda: (demo.parte2A(self), opcion_A.destroy(), opcion_B.destroy(), guardar.destroy()))
		opcion_A.place(x = 170, y = 540)
		opcion_B = tk.Button(self.canvas, text = 'No lo creo, la verdad es que suelo llegar tarde a la mayoría de los lugares a los que voy.', font = ('terminal', 15), width = 93, height = 2, bg = 'blue', fg = 'white', command = lambda: (demo.parte2B(self), opcion_A.destroy(), opcion_B.destroy(), guardar.destroy()))
		opcion_B.place(x = 170, y = 640)
		lugar = '1'
		guardar = tk.Button(self.canvas, text = 'Guardar', font = ('terminal', 15), bg = 'blue', fg = 'white', command = lambda: (demo.guardar(self, lugar), guardar.destroy()))
		guardar.place(x = 1, y = 1)
	# Fin decision

	# Inicio de la opcion A

	def parte2A(self):
		heroina.quitar_heroina(self)
		heroina.img_Traje_Cita_Pos1_Ex5(self)
		escenarios.mostrar_cuadro_texto(self)
		demo.poner_nombre(self, 'Hana')
		##
		texto = 'Ah? La perfección no existe.'
		self.mensaje = self.canvas.create_text(660, 600, text = texto, font = ('fangsong ti', 14), fill = 'white')
		# Boton
		b_siguiente = tk.Button(self.ventana, image = self.siguiente, command = lambda: (demo.parte2A_1(self), b_siguiente.destroy()))
		b_siguiente.place(x = 1155, y = 635)

	def parte2A_1(self):
		heroina.quitar_heroina(self)
		heroina.img_Traje_Cita_Pos1_Ex4(self)
		escenarios.sacar_cuadro_texto(self)
		escenarios.mostrar_cuadro_texto(self)
		demo.quitar_nombre_mensaje(self)
		demo.poner_nombre(self, 'Hana')
		##
		texto = 'Es mejor vivir el momento, no planeando tanto a futuro.'
		self.mensaje = self.canvas.create_text(660, 600, text = texto, font = ('fangsong ti', 14), fill = 'white')
		# Botones
		b_anterior = tk.Button(self.ventana, image = self.anterior, command = lambda: (demo.quitar_nombre_mensaje(self), escenarios.sacar_cuadro_texto(self), demo.parte2A(self), b_siguiente.destroy(), b_anterior.destroy()))
		b_anterior.place(x = 1100, y = 635)
		b_siguiente = tk.Button(self.ventana, image = self.siguiente, command = lambda: (demo.decision2A(self), b_siguiente.destroy(), b_anterior.destroy()))
		b_siguiente.place(x = 1155, y = 635)
		# Fin Botones

	# Fin de la decision A

	# Inicion de la decision B

	def parte2B(self):
		heroina.quitar_heroina(self)
		heroina.img_Traje_Cita_Pos2_Ex3(self)
		escenarios.mostrar_cuadro_texto(self)
		demo.poner_nombre(self, 'Hana')
		##
		texto = '¿Llegaste temprano solo por mi?'
		self.mensaje = self.canvas.create_text(660, 600, text = texto, font = ('fangsong ti', 14), fill = 'white')
		# Boton
		b_siguiente = tk.Button(self.ventana, image = self.siguiente, command = lambda: (demo.decision2B(self), b_siguiente.destroy()))
		b_siguiente.place(x = 1155, y = 635)

	# Fin de la decision B

	# Decisiones

	def decision2A(self):
		escenarios.sacar_cuadro_texto(self)
		demo.quitar_nombre_mensaje(self)
		opcion_A = tk.Button(self.canvas, text = '¿Eh? Ah... Tienes razón ¡Lo siento!', font = ('terminal', 15), width = 93, height = 2, bg = 'blue', fg = 'white', command = lambda: (demo.parte3A_A(self), opcion_A.destroy(), opcion_B.destroy(), guardar.destroy()))
		opcion_A.place(x = 170, y = 540)
		opcion_B = tk.Button(self.canvas, text = 'La perfección existe, yo soy perfecto.', font = ('terminal', 15), width = 93, height = 2, bg = 'blue', fg = 'white', command = lambda: (demo.parte3A_B(self), opcion_A.destroy(), opcion_B.destroy(), guardar.destroy()))
		opcion_B.place(x = 170, y = 640)
		lugar = '2A'
		guardar = tk.Button(self.canvas, text = 'Guardar', font = ('terminal', 15), bg = 'blue', fg = 'white', command = lambda: (demo.guardar(self, lugar), guardar.destroy()))
		guardar.place(x = 1, y = 1)

	def decision2B(self):
		escenarios.sacar_cuadro_texto(self)
		demo.quitar_nombre_mensaje(self)
		opcion_A = tk.Button(self.canvas, text = 'Pues claro... ¿Está mal?', font = ('terminal', 15), width = 93, height = 2, bg = 'blue', fg = 'white', command = lambda: (demo.parte3B_A(self), opcion_A.destroy(), opcion_B.destroy(), guardar.destroy()))
		opcion_A.place(x = 170, y = 540)
		opcion_B = tk.Button(self.canvas, text = '¡Claro que si! Eres muy especial para mi.', font = ('terminal', 15), width = 93, height = 2, bg = 'blue', fg = 'white', command = lambda: (demo.parte3B_B(self), opcion_A.destroy(), opcion_B.destroy(), guardar.destroy()))
		opcion_B.place(x = 170, y = 640)
		lugar = '2B'
		guardar = tk.Button(self.canvas, text = 'Guardar', font = ('terminal', 15), bg = 'blue', fg = 'white', command = lambda: (demo.guardar(self, lugar), guardar.destroy()))
		guardar.place(x = 1, y = 1)

	# Fin decisiones

	# Decisión A - decision2A
	def parte3A_A(self):
		heroina.quitar_heroina(self)
		heroina.img_Traje_Cita_Pos1_Ex8(self)
		escenarios.mostrar_cuadro_texto(self)
		demo.poner_nombre(self, 'Hana')
		##
		texto = 'No tienes que ser tan dramático... Aburrido'
		self.mensaje = self.canvas.create_text(660, 600, text = texto, font = ('fangsong ti', 14), fill = 'white')
		# Botón
		b_siguiente = tk.Button(self.ventana, image = self.siguiente, command = lambda: (demo.parte4(self), b_siguiente.destroy()))
		b_siguiente.place(x = 1155, y = 635)

	# Decisión B - decision2A
	def parte3A_B(self):
		heroina.quitar_heroina(self)
		heroina.img_Traje_Cita_Pos1_Ex2(self)
		escenarios.mostrar_cuadro_texto(self)
		demo.poner_nombre(self, 'Hana')
		##
		texto = 'Está bien, señor perfecto jajaja'
		self.mensaje = self.canvas.create_text(660, 600, text = texto, font = ('fangsong ti', 14), fill = 'white')
		# Botón 
		b_siguiente = tk.Button(self.ventana, image = self.siguiente, command = lambda: (demo.parte4(self), b_siguiente.destroy()))
		b_siguiente.place(x = 1155, y = 635)

	# Decisión A - decision2B
	def parte3B_A(self):
		heroina.quitar_heroina(self)
		heroina.img_Traje_Cita_Pos1_Ex13(self)
		escenarios.mostrar_cuadro_texto(self)
		demo.poner_nombre(self, 'Hana')
		##
		texto = '¡Claro que no! Es muy lindo de tu parte.'
		self.mensaje = self.canvas.create_text(660, 600, text = texto, font = ('fangsong ti', 14), fill = 'white')
		# Botón
		b_siguiente = tk.Button(self.ventana, image = self.siguiente, command = lambda: (demo.parte4(self), b_siguiente.destroy()))
		b_siguiente.place(x = 1155, y = 635)

	# Decisión B - decision2B
	def parte3B_B(self):
		# Quitar
		heroina.quitar_heroina(self)
		# Poner
		heroina.img_Traje_Cita_Pos1_Ex18(self)
		escenarios.mostrar_cuadro_texto(self)
		demo.poner_nombre(self, 'Hana')
		##
		texto = 'Vaya... Eres eres bastante directo.'
		self.mensaje = self.canvas.create_text(660, 600, text = texto, font = ('fangsong ti', 14), fill = 'white')
		# Botón
		b_siguiente = tk.Button(self.ventana, image = self.siguiente, command = lambda: (demo.parte4(self), b_siguiente.destroy()))
		b_siguiente.place(x = 1155, y = 635)

	# Continuación
	def parte4(self):
		# Quitar
		heroina.quitar_heroina(self)
		escenarios.sacar_cuadro_texto(self)
		demo.quitar_nombre_mensaje(self)
		# Poner
		heroina.img_Traje_Cita_Pos1_Ex2(self)
		escenarios.mostrar_cuadro_texto(self)
		demo.poner_nombre(self, 'Hana')
		texto = 'En fin... ¿Dónde iremos ahora?'
		self.mensaje = self.canvas.create_text(660, 600, text = texto, font = ('fangsong ti', 14), fill = 'white')
		# Botón
		b_siguiente = tk.Button(self.ventana, image = self.siguiente, command = lambda: (demo.parte4_1(self), b_siguiente.destroy()))
		b_siguiente.place(x = 1155, y = 635)

	def parte4_1(self):
		# Quitar
		demo.quitar_nombre_mensaje(self)
		# Poner
		demo.poner_nombre(self, self.nombre_prota)
		texto = 'Pues podriamos ir a tomar un helado.\n¿Qué te parece?'
		self.mensaje = self.canvas.create_text(660, 600, text = texto, font = ('fangsong ti', 14), fill = 'white')
		# Botones
		b_anterior = tk.Button(self.ventana, image = self.anterior, command = lambda: (demo.parte4(self), b_anterior.destroy(), b_siguiente.destroy()))
		b_anterior.place(x = 1100, y = 635)
		b_siguiente = tk.Button(self.ventana, image = self.siguiente, command = lambda: (demo.parte4_2(self), b_siguiente.destroy(), b_anterior.destroy()))
		b_siguiente.place(x = 1155, y = 635)

	def parte4_2(self):
		# Quitar
		demo.quitar_nombre_mensaje(self)
		# Poner
		demo.poner_nombre(self, 'Hana')
		texto = 'Me parece una excelente idea '+str(self.nombre_prota)+', vayamos por esos helados.'
		self.mensaje = self.canvas.create_text(660, 600, text = texto, font = ('fangsong ti', 14), fill = 'white')
		# Botones
		b_anterior = tk.Button(self.ventana, image = self.anterior, command = lambda: (demo.parte4_1(self), b_anterior.destroy(), b_siguiente.destroy()))
		b_anterior.place(x = 1100, y = 635)
		b_siguiente = tk.Button(self.ventana, image = self.siguiente)
		b_siguiente.place(x = 1155, y = 635)