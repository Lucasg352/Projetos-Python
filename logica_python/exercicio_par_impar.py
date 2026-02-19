"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_1=input('Digite um número inteiro:')

try:
    numero_int = int(numero_1)

    if numero_int % 2 == 0:
        print(f'O número {numero_1} é PAR')
    elif numero_int % 2 == 1:
        print(f'O número {numero_1} é IMPAR')
    else:
        print('Número não inteiro')

except:
    print('Não é um número inteiro')
