# gerador de senhas

'''import random
import string

alfabeto = string.ascii_letters
pontos = string.punctuation
alfa_pont = alfabeto + pontos

print("".join(random.SystemRandom().choices(alfa_pont, k=8)))'''


# gerador de senhas

import random
import string

alfabeto = string.ascii_letters
pontos = string.punctuation
alfa_pont = alfabeto + pontos

numero = int(input("Digite a quantidade de caracteres: "))

print("".join(random.SystemRandom().choices(alfa_pont, k=numero)))