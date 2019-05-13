#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk, font
import getpass
import subprocess, shlex


# Gestor de geometría (pack)


class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("RSA")
        
        #self.iniSockets()

        # Cambia el formato de la fuente actual a negrita para
        # resaltar las dos etiquetas que acompañan a las cajas
        # de entrada. (Para este cambio se ha importado el
        # módulo 'font' al comienzo del programa):

        fuente = font.Font(weight='bold')
        self.pbKeysDis = StringVar()

        # Define las etiquetas que acompañan a las cajas de
        # entrada y asigna el formato de fuente anterior:

        self.labelMsg = ttk.Label(self.raiz, text="Insert your Message",
                                  font=fuente)
        self.labelGetPubKeys = ttk.Label(self.raiz, text="Public Keys",
                                         font=fuente)
        self.LbPubKeys = ttk.Label(self.raiz, textvariable=self.pbKeysDis,
                                   font=fuente)
        self.LbEncryMsg = ttk.Label(self.raiz, text="",
                                   font=fuente)

        # Declara dos variables de tipo cadena para contener
        # el usuario y la contraseña:

        self.mensajeEnviado = StringVar()
        self.n = StringVar()
        self.k = StringVar()

        # Realiza una lectura del nombre de usuario que
        # inició sesión en el sistema y lo asigna a la
        # variable 'self.usuario' (Para capturar esta
        # información se ha importando el módulo getpass
        # al comienzo del programa):

        # self.mensajeEnviado.set(getpass.getuser())

        # Define dos cajas de entrada que aceptarán cadenas
        # de una longitud máxima de 30 caracteres.
        # A la primera de ellas 'self.ctext1' que contendrá
        # el nombre del usuario, se le asigna la variable
        # 'self.usuario' a la opción 'textvariable'. Cualquier
        # valor que tome la variable durante la ejecución del
        # programa quedará reflejada en la caja de entrada.
        # En la segunda caja de entrada, la de la contraseña,
        # se hace lo mismo. Además, se establece la opción
        # 'show' con un "*" (asterisco) para ocultar la
        # escritura de las contraseñas:

        self.ctext1 = ttk.Entry(self.raiz,
                                textvariable=self.mensajeEnviado,
                                width=30)
        self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)
        self.separ2 = ttk.Separator(self.raiz, orient=HORIZONTAL)

        # Se definen dos botones con dos métodos: El botón
        # 'Aceptar' llamará al método 'self.aceptar' cuando
        # sea presionado para validar la contraseña; y el botón
        # 'Cancelar' finalizará la aplicación si se llega a
        # presionar:

        self.btnGetPubKeys = ttk.Button(self.raiz, text="Get Public Key",
                                        command=self.getPublicKeys)
        self.btnEncrypth = ttk.Button(self.raiz, text="Encrypth Message",
                                        command=self.encrypthMesg)

        # Se definen las posiciones de los widgets dentro de
        # la ventana. Todos los controles se van colocando
        # hacia el lado de arriba, excepto, los dos últimos,
        # los botones, que se situarán debajo del último 'TOP':
        # el primer botón hacia el lado de la izquierda y el
        # segundo a su derecha.
        # Los valores posibles para la opción 'side' son:
        # TOP (arriba), BOTTOM (abajo), LEFT (izquierda)
        # y RIGHT (derecha). Si se omite, el valor será TOP
        # La opción 'fill' se utiliza para indicar al gestor
        # cómo expandir/reducir el widget si la ventana cambia
        # de tamaño. Tiene tres posibles valores: BOTH
        # (Horizontal y Verticalmente), X (Horizontalmente) e
        # Y (Verticalmente). Funcionará si el valor de la opción
        # 'expand' es True.
        # Por último, las opciones 'padx' y 'pady' se utilizan
        # para añadir espacio extra externo horizontal y/o
        # vertical a los widgets para separarlos entre sí y de
        # los bordes de la ventana. Hay otras equivalentes que
        # añaden espacio extra interno: 'ipàdx' y 'ipady':

        self.labelGetPubKeys.pack(side=TOP, fill=X, expand=True,
                                  padx=5, pady=5)
        self.btnGetPubKeys.pack(side=TOP, fill=X, expand=True,
                                padx=5, pady=5)
        self.separ2.pack(side=TOP, fill=X, expand=True,
                         padx=5, pady=5)
        self.LbPubKeys.pack(side=TOP, fill=X, expand=True,
                            padx=5, pady=5)
        self.labelMsg.pack(side=TOP, fill=X, expand=True,
                           padx=5, pady=5)
        self.ctext1.pack(side=TOP, fill=X, expand=True,
                         padx=5, pady=5)
        self.btnEncrypth.pack(side=TOP, fill=X, expand=True,
                                padx=5, pady=5)
        self.separ1.pack(side=TOP, fill=BOTH, expand=True,
                         padx=5, pady=5)
        self.LbEncryMsg.pack(side=TOP, fill=X, expand=True,
                            padx=5, pady=5)

        # Cuando se inicia el programa se asigna el foco
        # a la caja de entrada de la contraseña para que se
        # pueda empezar a escribir directamente:

        self.ctext1.focus_set()

        self.raiz.mainloop()

    # El método 'aceptar' se emplea para validar la
    # contraseña introducida. Será llamado cuando se
    # presione el botón 'Aceptar'. Si la contraseña
    # coincide con la cadena 'tkinter' se imprimirá
    # el mensaje 'Acceso permitido' y los valores
    # aceptados. En caso contrario, se mostrará el
    # mensaje 'Acceso denegado' y el foco volverá al
    # mismo lugar.

    def encrypthMesg(self):
        temp_msg = self.mensajeEnviado.get()
        n_temp = self.n.get()
        k_temp = self.k.get()
        #cadena_encrypt = './sendData' + ' ' + temp_msg + ' ' + n_temp + ' ' +k_temp
        #print(cadena_encrypt)
        result = subprocess.run(['./sendData', n_temp, k_temp, temp_msg], stdout=subprocess.PIPE)
        display = result.stdout.decode("utf-8")
        print(display)
        #pbKeys = display.split("\n")[0].split(" ")

        #pass

    def getPublicKeys(self):
        result = subprocess.run(['./getPublicKey'], stdout=subprocess.PIPE)
        display = result.stdout.decode("utf-8")
        print(display)
        pbKeys = display.split("\n")[0].split(" ")
        #print(pbKeys)
        self.pbKeysDis.set(display)
        return self.n.set(pbKeys[0]), self.k.set(pbKeys[1])
    
    def iniSockets(self):
        pass


def main():
    mi_app = Aplicacion()
    return 0


if __name__ == '__main__':
    main()
