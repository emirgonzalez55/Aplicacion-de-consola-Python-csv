import csv
import operator
import pandas as pd

ultima_id = 0

class Participantes:

    def __init__(self, nro_de_participante, nombre, apellido, edad, sexo):
        self.nro_de_participante = nro_de_participante
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo



class Torneo:
    def nuevo_participante(self, NroPart,Nombre,Apellido,Edad,Sexo,Disp1,Disp2,Disp3):
        
    
        with open("participantes.csv") as archivo:
            mensaje = "\n" + NroPart + "," + Nombre + "," + Apellido + "," + Edad + "," + Sexo + "," + Disp1 + "," + Disp2 + "," + Disp3
            with open("participantes.csv", "a") as archivo:
                writer = csv.writer(archivo)
                archivo.write(mensaje)           

    def mostrar_participantes(self):
        datos=pd.read_csv('participantes.csv' ,header=0)
        print(datos)

    def podio(self):
        datos=pd.read_csv('participantes.csv' ,header=0)
        datos=datos.sort_values(by='PromDisp', ascending=False)
        datos.head(3)
        print(datos.head(3))


    def cantidad_participantes(self):
        datos = pd.read_csv('participantes.csv')
        print("Cantidad de participantes:", len(datos.index))

    def participantes_por_edad(self):
        datos=pd.read_csv('participantes.csv' ,header=0)
        print(datos.sort_values(by='Edad', ascending=False))

    def promedio_disparos(self): 
        datos=pd.read_csv('participantes.csv')
        datos = datos['PromDisp'].mean()
        print("El promedio de todos los disparos es=",datos)