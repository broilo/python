# Criar um programa que faça o computador jogar jokenpô contigo.

import random
from time import sleep
print('\033[1;34m='*20, 'Jokenpô ', '='*20 )
print('''\033[1;4;32mRegras\033[1;32m: 
(*) pedra < papel < tesoura < pedra
(*) papel < tesoura < pedra < papel
(*) tesoura < pedra < papel < tesoura''')
o1 = str('pedra')
o2 = str('papel')
o3 = str('tesoura')
opções = [o1, o2, o3]
comp = random.choice(opções)
human = str(input('\033[1;34mDigite a tua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if human == o2 and comp == o1 or human == o3 and comp == o2 or human == o1 and comp == o3:
    print('\033[1;31mTu ganhaste pois {} vence {}!'.format(human, comp))
elif comp == o2 and human == o1 or comp == o3 and human == o2 or comp == o1 and human == o3:
    print('\033[1;31mTu perdeste pois {} perde para {}!'.format(human, comp))
elif human == comp:
    print('\033[1;31mEmpate, pois {} e {} são iguais'.format(human, comp))
elif human == 'lizard' or human == 'spock':
    print('\033[1;31mHAhhahHAHAHhaH, ganhaste pela criatividade!')
else:
    print('\033[1;31mTu digitaste errado! Tente novamente!')
