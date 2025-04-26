informe = int(input('Informe um número: '))
resto = informe % 3
match resto :
    case 0:
        print('Esse número é multiplo de 3')
    case _:
        print('Esse número não é multiplo de 3')