from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
comp = randint(0, 2)
print(itens[comp])
print('''Tuas opções:
[0] pedra
[1] papel
[2] tesoura ''')
jogador = int(input('Qual é a tua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-' * 8)
print('Computador jogou {}.'.format(itens[comp]))
print('Jogador jogou {}.'.format(itens[jogador]))
print('-=-' * 8)
if comp == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador vence')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('Jogada inválida.')
elif comp == 1:
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador vence')
    else:
        print('Jogada inválida.')

elif comp == 2:
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada inválida.')
