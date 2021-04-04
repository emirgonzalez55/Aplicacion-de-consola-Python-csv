import sys
from clases import Torneo, Participantes

class Menu:
    def __init__(self):
        self.clases = Torneo()
        self.elecciones = {
                "1" : self.participantes,
                "2" : self.mostrar_participantes,
                "3" : self.podio, 
                "4" : self.cantidad_participantes,
                "5" : self.participantes_por_edad,
                "6" : self.promedio_disparos,  					
                "7" : self.quit
                } 

    def mostrar_menu(self):
        print("""
Menu Torneo

1 Agregar participantes
2 Mostrar participantes
3 Mostrar podio
4 Mostras cantidad de participantes
5 Participantes ordenados por edad
6 Promedio de todos los disparos 
7 Salir
""")

    def run(self):
        while True:
            self.mostrar_menu()
            eleccion = input("Escribe una opción: ")
            accion = self.elecciones.get(eleccion)
            if accion:
                accion()
            else:
                print("{0} no es una elección válida".format(eleccion))

    

    def participantes(self):
        NroPart = input("Escriba el numero: ")
        Nombre = input("Escriba un nombre: ")
        Apellido = input("Escriba apellido: ")
        Edad = input("Escriba edad: ")
        Sexo = input("Escriba sexo: ")
        Disp1 = input("Escriba Disp1: ")
        Disp2 = input("Escriba Disp2: ")
        Disp3 = input("Escriba Disp3: ")
        self.clases.nuevo_participante(NroPart,Nombre,Apellido,Edad,Sexo,Disp1,Disp2,Disp3)
        print("Participante añadido.") 

    def mostrar_participantes(self):  
    	self.clases.mostrar_participantes()

    def podio(self):  
    	self.clases.podio()

    def cantidad_participantes(self):
    	self.clases.cantidad_participantes()	

    def participantes_por_edad(self):
    	self.clases.participantes_por_edad()

    def promedio_disparos(self):
    	self.clases.promedio_disparos()


    def quit(self):
        print("Aplicacion cerrada.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()