
while True:
    a = float(input('Digite o primeiro numero: '))
    b = float(input('Digite o segundo numero: '))

    print('1 - soma')
    print('2 - subtração')
    print('3 - multiplicação')
    print('4 - divisão')
    print('5 - Sair')
    opcao = int(input('Escolha uma das opções acima: '))

    match opcao:
        case 1:
            print(f'Resultado da soma é {a + b}')
        case 2:
            print(f'Resultado da subtração é {a - b}')
        case 3:
            print(f'Resultado da multiplicação é {a * b}')
        case 4:
            if b != 0:
                print(f'Resultado da divisão é {a / b}')
            else:
                print('Não é possivel fazer uma divisão por zero')
        case 5:
            print("Obrigado por usar o sistema de calculador!!!!")
            break
        case _:
            print('Opção inválida')
