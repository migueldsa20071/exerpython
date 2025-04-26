"""
Solicite dois números inteiros ao usuário e exiba apenas o maior deles.
Caso eles sejam iguais exiba a mensagem “Números Iguais”.
"""
num1 = int(input('Escolha o primeiro número: '))
num2 = int(input('Escolha o segundo número: '))

if num1 > num2:
    print(f'{num1}é maior que o {num2}')
elif num2 > num1:
    print(f'{num2} é maior que o {num1}')
else :
    print('os Números são iguais')