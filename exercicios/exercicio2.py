'''2. Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;'''


class Quadrado:
    '''classe que modela um quadrado'''
    def __init__(self, lado): #método construtor da classe
        self.lado = lado

    def mudar_lado(self, novo_lado):
        self.mudar = novo_lado

    def retornar_lado(self):
        return self.lado

    def calcular_area(self):
        return self.lado**2
    
    

qdd1 = Quadrado(5)

print("Lado do quadrado: ", qdd1.retornar_lado())


qdd1.mudar_lado(10)
print("Novo lado do quadrado:", qdd1.retornar_lado())


area = qdd1.calcular_area()
print("Área do quadrado: ", area)