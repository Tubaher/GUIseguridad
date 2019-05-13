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

        # Define las etiquetas que acompañan a las cajas de
        # entrada y asigna el formato de fuente anterior:

        self.labelParameters = ttk.Label(self.raiz, text="Insert Parameters",
                                  font=fuente)        
        self.labelEncrypted = ttk.Label(self.raiz, text="Encrypted Message",
                                         font=fuente)
        self.labelDecrypt = ttk.Label(self.raiz, text="Decrypted Message",
                                  font=fuente)    
                      
                   

        # Declara dos variables de tipo cadena para contener
        # el usuario y la contraseña:

        self.dencryptedMessage = StringVar()
        self.encryptedMessage = StringVar()

        self.labelEncryptedMsg = ttk.Label(self.raiz, textvariable=self.encryptedMessage,
                                         font=fuente)
        self.labelDecryptMsg = ttk.Label(self.raiz, textvariable=self.dencryptedMessage ,
                                  font=fuente) 

        self.n = StringVar()
        self.k = StringVar()
        self.j = StringVar()

                     
        self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)
        self.separ2 = ttk.Separator(self.raiz, orient=HORIZONTAL)

        # Se definen dos botones con dos métodos: El botón
        # 'Aceptar' llamará al método 'self.aceptar' cuando
        # sea presionado para validar la contraseña; y el botón
        # 'Cancelar' finalizará la aplicación si se llega abu
        # presionar:

        self.btnDecrypt = ttk.Button(self.raiz, text="Run Server",
                                        command=self.cmdDecryptMessg)
        
        self.btnRunDecrypt = ttk.Button(self.raiz, text="Run Server Decrypt",
                                        command=self.cmdRunDecryptMessg)



        self.labelParameters.pack(side=TOP, fill=X, expand=True,
                                  padx=5, pady=5)

        self.framen = ttk.Frame(self.raiz)
        self.framen.pack(fill=X)

        self.labeln = ttk.Label(self.framen, text="n", width=4) 
        self.labeln.pack(side=LEFT ,padx=5, pady=5)

        self.labelnValue = ttk.Label(self.framen,textvariable=self.n, width=4)
        self.labelnValue.pack(fill=X, expand=True, padx=5, pady=5)

        self.framek = ttk.Frame(self.raiz)
        self.framek.pack(fill=X)

        self.labelk = ttk.Label(self.framek, text="k", width=4) 
        self.labelk.pack(side=LEFT ,padx=5, pady=5)

        self.labelkValue = ttk.Label(self.framek,textvariable=self.k, width=4)
        self.labelkValue.pack(fill=X, expand=True, padx=5, pady=5)

        self.framej = ttk.Frame(self.raiz)
        self.framej.pack(fill=X)

        self.labelj = ttk.Label(self.framej, text="j", width=4) 
        self.labelj.pack(side=LEFT ,padx=5, pady=5)

        self.labeljValue = ttk.Label(self.framej,textvariable=self.j, width=4)
        self.labeljValue.pack(fill=X, expand=True, padx=5, pady=5)

        self.labelEncrypted.pack(fill=X,padx=5, pady=5)
        self.labelEncryptedMsg.pack(fill=X,padx=5, pady=5)

        self.btnDecrypt.pack(fill=X,padx=5, pady=5)
        self.btnRunDecrypt.pack(fill=X,padx=5, pady=5)


        self.labelDecrypt.pack(fill=X,padx=5, pady=5)
        self.labelDecryptMsg.pack(fill=X,padx=5, pady=5)


        




        # Cuando se inicia el programa se asigna el foco
        # a la caja de entrada de la contraseña para que se
        # pueda empezar a escribir directamente:


        self.raiz.mainloop()

    # El método 'aceptar' se emplea para validar la
    # contraseña introducida. Será llamado cuando se
    # presione el botón 'Aceptar'. Si la contraseña
    # coincide con la cadena 'tkinter' se imprimirá
    # el mensaje 'Acceso permitido' y los valores
    # aceptados. En caso contrario, se mostrará el
    # mensaje 'Acceso denegado' y el foco volverá al
    # mismo lugar.

    def cmdDecryptMessg(self):
        p1='5915587277'
        p2='1500450271'
        result = subprocess.run(['./Sockets', p1, p2], stdout=subprocess.PIPE)
        display = result.stdout.decode("utf-8")
        #print(display)
        display = display.split(' ')[2:]
        display[0] = display[0].split('\n')[1]
        display[2] = display[2].split('\n')[0]
        
        #seteo las llaves
        self.n.set(display[0])
        self.k.set(display[1])
        self.j.set(display[2])
        #print(display)
        """ temp_msg = self.dencryptedMessage.get()
        n_temp = self.n.get()
        k_temp = self.k.get() """
        #cadena_encrypt = './sendData' + ' ' + temp_msg + ' ' + n_temp + ' ' +k_temp
        #print(cadena_encrypt)
       
        #pbKeys = display.split("\n")[0].split(" ")

        #pass

    
    def cmdRunDecryptMessg(self):
        p1='5915587277'
        p2='1500450271'
        result = subprocess.run(['./Sockets', p1, p2], stdout=subprocess.PIPE)
        display = result.stdout.decode("utf-8")
        display = display.split('\n')[2:len(display)-2]
        self.encryptedMessage.set(display[0])
        self.dencryptedMessage.set(display[1])
        print(display)
        # display = display.split(' ')[2:]
        # display[0] = display[0].split('\n')[1]
        # display[2] = display[2].split('\n')[0]
        
        #seteo las llaves
        # self.n.set(display[0])
        # self.k.set(display[1])
        # self.j.set(display[2])
        #print(display)
        """ temp_msg = self.dencryptedMessage.get()
        n_temp = self.n.get()
        k_temp = self.k.get() """
        #cadena_encrypt = './sendData' + ' ' + temp_msg + ' ' + n_temp + ' ' +k_temp
        #print(cadena_encrypt)

        #pbKeys = display.split("\n")[0].split(" ")
        #pass
    
    def iniSockets(self):
        pass


def main():
    mi_app = Aplicacion()
    return 0


main()
