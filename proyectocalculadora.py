from tkinter import *

ventana=Tk()

i = 0

#Entrada 
entradat = Entry(ventana, font= ("Calibri 20"))
entradat.grid(row= 0, column= 0, columnspan= 4, padx= 50, pady= 5)

#Funciones
def hover(valor):
    global i
    entradat.insert(i, valor)
    i +=1
    
def borrar():
    entradat.delete(0, END)
    i =0

def operacion():
    ecuacion = entradat.get() 
    resultado = eval(ecuacion)
    entradat.delete(0, END)
    entradat.insert(0, resultado)
    i = 0

#Botones
boton1 = Button(ventana, text= "1", width=5, height= 2, command= lambda: hover(1))
boton2 = Button(ventana, text= "2", width=5, height= 2, command= lambda: hover(2))
boton3 = Button(ventana, text= "3", width=5, height= 2, command= lambda: hover(3))
boton4 = Button(ventana, text= "4", width=5, height= 2, command= lambda: hover(4))
boton5 = Button(ventana, text= "5", width=5, height= 2, command= lambda: hover(5))
boton6 = Button(ventana, text= "6", width=5, height= 2, command= lambda: hover(6))
boton7 = Button(ventana, text= "7", width=5, height= 2, command= lambda: hover(7))
boton8 = Button(ventana, text= "8", width=5, height= 2, command= lambda: hover(8))
boton9 = Button(ventana, text= "9", width=5, height= 2, command= lambda: hover(9))
boton0 = Button(ventana, text= "0", width=20, height= 2, command= lambda: hover(0))

botonborrar = Button(ventana, text= "AC", width=5, height= 2, command= lambda: borrar())
botonparentesis1 = Button(ventana, text= "(", width=5, height= 2, command= lambda: hover("("))
botonparentesis2 = Button(ventana, text= ")", width=5, height= 2, command= lambda: hover(")"))
botonpunto = Button(ventana, text= ".", width=5, height= 2, command= lambda: hover("."))

botondivision = Button(ventana, text=chr(247), width=5, height= 2, command= lambda: hover("/"))
botonmultiplicacion = Button(ventana, text= "x", width=5, height= 2, command= lambda: hover("*"))
botonsuma = Button(ventana, text= "+", width=5, height= 2, command= lambda: hover("+"))
botonresta = Button(ventana, text= "-", width=5, height= 2, command= lambda: hover("-"))
botonigual = Button(ventana, text= "=", width=5, height= 2, command= lambda: operacion())

#Agregar botones en pantalla
botonborrar.grid(row = 1, column = 0, padx = 5, pady = 5)
botonparentesis1.grid(row = 1, column = 1, padx = 5, pady = 5)
botonparentesis2.grid(row = 1, column = 2, padx = 5, pady = 5)
botondivision.grid(row = 1, column = 3, padx = 5, pady = 5)

boton7.grid(row = 2, column = 0, padx = 5, pady = 5)
boton8.grid(row = 2, column = 1, padx = 5, pady = 5)
boton9.grid(row = 2, column = 2, padx = 5, pady = 5)
botonmultiplicacion.grid(row = 2, column = 3, padx = 5, pady = 5)

boton4.grid(row = 3, column = 0, padx = 5, pady = 5)
boton5.grid(row = 3, column = 1, padx = 5, pady = 5)
boton6.grid(row = 3, column = 2, padx = 5, pady = 5)
botonsuma.grid(row = 3, column = 3, padx = 5, pady = 5)

boton1.grid(row = 4, column = 0, padx = 5, pady = 5)
boton2.grid(row = 4, column = 1, padx = 5, pady = 5)
boton3.grid(row = 4, column = 2, padx = 5, pady = 5)
botonresta.grid(row = 4, column = 3, padx = 5, pady = 5)

boton0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
botonpunto.grid(row = 5, column = 2, padx = 5, pady = 5)
botonigual.grid(row = 5, column = 3, padx = 5, pady = 5)

ventana.mainloop()
