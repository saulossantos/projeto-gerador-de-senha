# gerador de senhas, somente com 11 números e validar se não é um CPF


import string
import random 
from random import randint

caracteres = string.digits
lista_caracteres = [caracteres]

quantidade = 11

for c in caracteres:
    random.shuffle(lista_caracteres)
    lista_caracteres.append(c)
    
senha = []

for i in range(quantidade):
    senha.append(random.choice(lista_caracteres))
    random.shuffle(senha)
    
print("".join(senha))

def validar_cpf(senha):
    senha = [int(char) for char in senha if char.isdigit()]

    if len(senha) != 11:
        return False

    if senha == senha[::-1]:
        return False

    for i in range(9, 11):
        valor = sum((senha[num] * ((i+1) - num) for num in range(0, i)))
        digitos = ((valor * 10) % 11) % 10
        if digitos != senha[i]:
            return False
    return True

if validar_cpf(senha): 
    print('A senha é um CPF')
else:
    print('A senha não é um CPF')