# gerador de senhas, somente números

import random
import string

caracteres = string.digits
lista_caracteres = [caracteres]

quantidade = int(input("Digite a quantidade de caracteres: "))

print("".join(random.SystemRandom().choices(caracteres, k=quantidade)))