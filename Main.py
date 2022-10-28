import tkinter as tk
import Escenarios as sitios
import Heroina as tipas
import Demo as demo
import Cargar as cargar

# Caracteristicas meh de la ventana
ventana = tk.Tk()
ventana.geometry('1280x720')
ventana.resizable(False, False)
ventana.title('Lo pensaré mas adelante')
canvas = tk.Canvas(ventana, width = 1280, height = 720)
canvas.pack()
# Fin Caracteristicas meh de la ventana

# Programas de ajuera
IMG_sitios = sitios.escenarios(ventana, canvas)
IMG_tipas = tipas.heroina(canvas, ventana)
IMG_demo = demo.demo(ventana, canvas)
cargar = cargar.cargar(ventana, canvas)
# Fin programas de ajuera

# Imagen del menú principal
IMG_sitios.menu_Principal()
IMG_tipas.heroina_menu_principal()
# Fin imagen del menú principal

# Botones menú principal
img_boton_nuevaP = tk.PhotoImage(file = 'boton1.png')
img_boton_cargar = tk.PhotoImage(file = 'boton2.png')
img_boton_salir = tk.PhotoImage(file = 'boton3.png')
b_nuevo_juego = tk.Button(canvas, image = img_boton_nuevaP, command = lambda: IMG_demo.nuevo_juego())
b_nuevo_juego.place(x = 1040, y = 500)
b_cargar = tk.Button(canvas, image = img_boton_cargar, command = lambda: cargar.cargar_cargar())
b_cargar.place(x = 1040, y = 560)
b_salir = tk.Button(canvas, image = img_boton_salir, command = exit)
b_salir.place(x = 1040, y = 620)
# fin botones menú principal

ventana.mainloop()