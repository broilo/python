# Escrever um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5, e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
# venceu ou perdeu.

import random
print('Vou pensar em um número entre 0 e 5. \n Pronto, pensei! Agora tu tens de tentar descobrir...')
num1 = random.randint(0, 5)
# print(num1)
a1 = int(input('Digite um número entre 0 e 5: '))
if a1 == num1:
    print('Acertaste, {}={}.'.format(a1, num1))
else:
    print('Erraste, o número que pensei foi {}.'.format(num1))
