from tkinter import ttk
from tkinter import *

class Desk:
    def __init__(self, window):
        # Initializations
        
        #ancho
        ancho = 800
        
        #alto
        alto = 600
        
        # asignamos la ventana a una variable de la clase llamada wind
        self.wind = window

        #le asignamos el ancho y el alto a la ventana con la propiedad geometry
        self.wind.geometry(str(ancho)+'x'+str(alto))

        #centramos el contenido 
        self.wind.columnconfigure(0, weight=1)
        
        #le damos un titulo a la ventana
        self.wind.title('Aplicación con interface gráfica en Python - By christian Rivera')
        
        # creamos un contenedor
        frame = LabelFrame(self.wind, text = 'Sumar 2 valores')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        
        # creamos un etiqueta
        Label(frame, text = 'primer numero: ').grid(row = 1, column = 0)
        
        #creamos un input donde ingresar valores
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1, column = 1)
        
        # igual que arriba una etiqueta y un campo input para ingresar valores
        Label(frame, text = 'segundo numero: ').grid(row = 2, column = 0)
        self.var2 = Entry(frame)
        self.var2.grid(row = 2, column = 1)
        
        #Creamos un boton para ejecutar las operaciones
        Button(frame, text = 'Sumar', command = self.sumar).grid(row = 3, columnspan = 2, sticky = W + E)
        Button(frame, text = 'Restar', command = self.restar).grid(row = 4, columnspan = 3, sticky = W + E)
        Button(frame, text = 'Multiplicar', command = self.multiplicar).grid(row = 5, columnspan = 4, sticky = W + E)
        Button(frame, text = 'Dividir', command = self.dividir).grid(row = 6, columnspan = 5, sticky = W + E)
    
        #designamos un área para mensajes
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)
        
    # creamos una función para validar que los campos no esten en blanco
    def validation(self):
        return len(self.var1.get()) != 0 and len(self.var2.get()) != 0
    
    # esta es la función que ejecuta la suma
    def sumar(self):
        if self.validation():
            resultado = float( self.var1.get() ) + float( self.var2.get() )
            self.message['text'] = 'La suma de las 2 variables es: {}'.format(resultado)
        else:
            self.message['text'] = 'los campos son requeridos'
            # Aqui resta las cosas esas
    def restar(self):
        if self.validation():
            resultado = float( self.var1.get() ) - float( self.var2.get() )
            self.message['text'] = 'La resta  de las 2 variables es: {}'.format(resultado)
        else:
            self.message['text'] = 'los campos son requeridos'
    def multiplicar(self):
        if self.validation():
            resultado = float( self.var1.get() ) * float( self.var2.get() )
            self.message['text'] = 'La multiplicacion de las 2 variables es: {}'.format(resultado)
        else:
            self.message['text'] = 'los campos son requeridos'
    def dividir(self):
        if self.validation():
            resultado = float( self.var1.get() ) / float( self.var2.get() )
            self.message['text'] = 'La division de las 2 variables es: {}'.format(resultado)
        else:
            self.message['text'] = 'los campos son requeridos'
    
    
    
#validamos si estamos en la aplicación inicial
if __name__ == '__main__':
    
    #asignamos la propiedad de tkinter a la variable window
    window = Tk()
    
    #en la variable app guardamos la clase Desk y le enviamos como parametro la ventana 
    app = Desk(window)

    #ejecutamos un mainloop para que se ejecute la ventana
    window.mainloop()