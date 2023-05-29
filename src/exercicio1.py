# gerador de senhas, somente números e letras minúsculas 

import random
import string

caracteres = string.ascii_lowercase + string.digits
lista_caracteres = [caracteres]

quantidade = int(input("Digite a quantidade de caracteres: "))

print("".join(random.SystemRandom().choices(caracteres, k=quantidade)))