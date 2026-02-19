"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

"""

nome = input('Qual o nome do usuário?:')

contar_letras = len(nome) #variável usada para contar a quantidade de letras para ser exibida a seguir

if contar_letras <5 :
    print (f'O nome {nome} tem {contar_letras} letras e é um nome curto')
elif contar_letras <7:
    print (f'O nome {nome} tem {contar_letras} letras e é um nome normal')
else:
    print (f'O nome {nome} tem {contar_letras} letras e é muito grande')

#Escolhi deixar uma mensagem mais "elaborada" em cada condição
