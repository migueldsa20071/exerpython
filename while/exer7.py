"""
Faça um algoritmo que solicite um número inteiro e calcule seu fatorial.
O fatorial de um número N é a multiplicação de N por seus antecessores
maiores ou iguais a 1.
Por exemplo:
O fatorial de 5 é igual a 5*4*3*2*1 = 120.
"""

fatorial = 1  

num = int(input('Escolhe um número inteiro: '))

while num >=1: 
    fatorial *=num
    num -=1

print(f'A fatorial do número escolhido é {fatorial}')