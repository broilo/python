# Melhorar o jogo do Desafio 28 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador
# vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
from time import sleep
print("""\033[1;34mOlá, eu sou o Goku! Nááá, mentira, eu sou só o teu computador.
Eu vou pensar em um número entre 0 e 10...""")
sleep(2)
print('hmm')
sleep(1)
print('hmmmmmm')
sleep(1)
print('Pronto, já pensei! Tenta adivinhar, vai!')
num = random.randint(0, 10)
palpites = 0
acertou = False
while not acertou:
    num1 = int(input('\033[1;31mQual número tu achas que foi?: '))
    if num1 > num:
        print('\033[1;32m Pô, vacilão! Menos que isso! Tenta de novo!')
    elif num1 < num:
        print('\033[1;32m Vacilou goxtoso. É maior! Tenta mais outra vez!')
    if num1 == num:
        acertou = True
    palpites += 1
print('''\033[1;34mIssaê, acertou! Até que enfim! Ufa!
Mas óitchê, tu demorasse {} vezes até acertar!'''.format(palpites))
