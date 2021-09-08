import random
import string_utils

z = int(1)
while z != 0:
 
    senha = "abcdefghijklmnopqrstuvwxyz01234567890123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@!#$%&*+-/"

    tamanho = int(input("Deseja uma senha de que tamanho ?: "))
    string_utils.shuffle(senha)
    i = int(0)
    senha_str = str()
    while i < tamanho:
        senha_str = list(senha_str) + list(random.choice(senha))
        i = i + 1
    string_utils.shuffle(str(senha_str))
    print(''.join(senha_str))
    z = int(input("Deseja gerar outra senha?: 1 - sim/ 0 - nao: "))
