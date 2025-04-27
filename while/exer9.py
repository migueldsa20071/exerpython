'''
Fazer um algoritmo que solicite um número inteiro N qualquer e exiba a tabuada de N
Exemplo: para N = 7
7 x 1 = 7
7 x 2= 14 
7 x 10 = 70
'''

n = int(input('Escolha algum número inteiro: '))
v = 1

while v <= 10:
    t = n * v 
    print(f"{n} x {v} = {t}")
    v += 1