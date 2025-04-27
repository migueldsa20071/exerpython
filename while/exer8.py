'''
Fazer um algoritmo que exiba na tela todos os números ímpares de 1 a n, onde n é fornecido pelo usuário
'''

n = int(input('Escolha um número inteiro: '))
i = 1

while i <= n:
    if i % 2 != 0:
        print(i)
    i += 1