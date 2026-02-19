"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

"""

horario = input('Qual é o horário?:')

horario_int = int(horario)

if horario_int < 12:
    print (f'Bom dia, agora são {horario_int}h')
elif horario_int < 18:
    print(f'Boa tarde, agora são {horario_int}h')
else:
    print(f'Boa noite, agora são {horario_int}h')
