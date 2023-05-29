'''1. Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: troca Cor e mostra Cor'''


class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def troca_cor(self, nova_cor):
        self.cor = nova_cor
    
    def mostra_cor(self):
        return self.cor


bolinha = Bola("azul", 10, "plástico")
print("Cor da bola:", bolinha.mostra_cor())

bolinha.troca_cor("cinza")
print("Mudança de cor:", bolinha.mostra_cor())