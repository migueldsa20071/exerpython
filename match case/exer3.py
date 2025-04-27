'''
Faça um algoritmo que verifica se o número informado é multiplo de 3, utilizando o match case
'''

informe = int(input('Informe um número: '))
resto = informe % 3
match resto :
    case 0:
        print('Esse número é multiplo de 3')
    case _:
        print('Esse número não é multiplo de 3')