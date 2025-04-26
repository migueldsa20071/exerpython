'''
Escreva um Programa que, dados dois números inteiros, mostre na tela o maior deles, 
assim como a diferença existente entre ambos.
'''


num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O {num1} é maior que o {num2}')
    subtracao = num1 - num2
    print(f'A diferença entre eles é {subtracao}')
elif num2 > num1:
    print(f'O {num2} é maior que o {num1}')
    subtracao = num2 - num1
    print(f'A diferença entre eles é {subtracao}')
else:
    print('Ambos possuem o mesmo tamanho')