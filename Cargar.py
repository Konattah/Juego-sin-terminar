from Demo import *
from Heroina import *
from Escenarios import *

class cargar(demo):
	def __init__(self, ventana, canvas):
		demo.__init__(self, ventana, canvas)
		self.canvas = canvas
		self.ventana = ventana

	def cargar_cargar(self):
		partida = open('guardado/nombre.txt', 'r')
		nombre = partida.readline()
		demo.cargar(self, nombre)
		partida.close()

		partida = open('guardado/lugar.txt', 'r')
		lugar = partida.readline()
		partida.close()

		if(lugar == '1'):
			escenarios.img_fondo09(self)
			escenarios.mostrar_cuadro_texto(self)
			heroina.img_Traje_Cita_Pos1_Ex2(self)
			demo.decision1(self)

		elif(lugar == '2A'):
			escenarios.img_fondo09(self)
			escenarios.mostrar_cuadro_texto(self)
			heroina.img_Traje_Cita_Pos1_Ex4(self)
			demo.decision2A(self)

		elif(lugar == '2B'):
			escenarios.img_fondo09(self)
			escenarios.mostrar_cuadro_texto(self)
			heroina.img_Traje_Cita_Pos2_Ex3(self)
			demo.decision2B(self)