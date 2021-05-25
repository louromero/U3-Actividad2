from Sabor import Sabor
import csv

class ManejadorSabor:
    __sabores=[]

    def __init__(self):
        self.__sabores=[]


    def testSabores(self):
        archivo=open('sabores.csv')
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            nombre=fila[0]
            descripcion=fila[1]
            self.agregarSabor(Sabor(nombre,descripcion))

    def agregarSabor(self,sabor):
        self.__sabores.append(sabor)

    def getSabores(self):
        return self.__sabores

    def getSabor(self,identificador):
        identificador-=1
        return self.__sabores[identificador]