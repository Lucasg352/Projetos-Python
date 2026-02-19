"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_1=input('Digite um número inteiro:')

try: #Para "capturar" um possível futuro erro quando não for inserido um número inteiro
    numero_int = int(numero_1) # Uma variável feita para converter o retorno do input para int

    if numero_int % 2 == 0: #Checagem do resto da divisão
        print(f'O número {numero_1} é PAR')
    else:
        print('Número é IMPAR')

except: #Irá exibir a mensagem abaixo quando um número não inteiro for inserido que ocasionaria um erro
    print('Não é um número inteiro')
