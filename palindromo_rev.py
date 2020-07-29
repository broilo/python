# Criar um programa que leia uma frase qualquer e diga se ele é um palíndromo, desconsiderando os espaços.
#Ex: APOS A SOPA ; A SACADA DA CASA ; A TORRE DA DERROTA ; O LOBO AMA O BOLO ; ANOTARAM A DATA DA MARATONA.
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print('Temos um palíndromo, pois {} é igual à {}.'.format(junto, inverso))
else:
    print('Não temos um palíndromo, pois {} é diferente de {}.'.format(junto, inverso))
