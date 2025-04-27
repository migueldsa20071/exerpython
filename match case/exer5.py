'''
Faça um algoritmo que exiba um Menu com as opções de um cardápio de restaurante. O cliente deve escolher
o código do prato desejado e na sequência, informar se aceita pagar uma taxa de serviço de 10%. Se o usuário 
aceitar, mostrar o valor final (valor do prato +10% ), caso contrário, mostrar somente o valor do prato.
'''

print('1 - Picanha Valor: R$ 25')
print('2 - Lasanha Valor: R$ 20')
print('3 - Strogonoff  Valor: R$ 20')
print('4 - Bife Acebolado Valor: R$ 15')
print('5 - Pão com Ovo Valor: R$ 5')
menu = int(input('Escolha o Código do produto desejado: '))
aceita = int(input('aceita pagar uma taxa de serviço de 10%?\n Caso queira digite 1\n Caso não queira digite 2: '))


match menu: 
    case 1:
        preco = 25
        match aceita:
            case 1:
                taxa = preco + preco/100 * 10
                print(f'O valor a ser pago sera {taxa}')
            case 2:
                print(f'O valor a ser pago é {preco}')
            case _ :
                print('Opção inválida')
    case 2 :
        preco = 20
        match aceita:
            case 1:
                taxa = preco + preco/100 * 10
                print(f'O valor a ser pago sera {taxa}')
            case 2:
                print(f'O valor a ser pago é {preco}')
            case _ :
                print('Opção inválida')
    case 3 :
        preco = 20
        match aceita:
            case 1:
                taxa = preco + preco/100 * 10
                print(f'O valor a ser pago sera {taxa}')
            case 2:
                print(f'O valor a ser pago é {preco}')
            case _ :
                print('Opção inválida')
    case 4 :
        preco = 15
        match aceita:
            case 1:
                taxa = preco + preco/100 * 10
                print(f'O valor a ser pago sera {taxa}')
            case 2:
                print(f'O valor a ser pago é {preco}')
            case _ :
                print('Opção inválida')
    case 5:
        preco = 5
        match aceita:
            case 1:
                taxa = preco + preco/100 * 10
                print(f'O valor a ser pago sera {taxa}')
            case 2:
                print(f'O valor a ser pago é {preco}')
            case _ :
                print('Opção inválida')
    case _ :
        print('fora do cardápio')


'''
Tamém daria para fazer assim 
print('1  -  Picanha        R$ 25.00')
print('2  -  Lasanha        R$ 20.00')
print('3  -  Strogonoff     R$ 20.00')
print('4  -  Bife acebolado R$ 15.00')
print('5  -  Pao com ovo    R$  5.00')
opcao = int(input('Escolha o prato: '))
match opcao:
    case 1:
        valor = 25
    case 2 | 3:
        valor = 20
    case 4:
        valor = 15
    case 5:
        valor = 5
    case _:
        valor = 0
        print('Prato inexistente')

taxa = input('Deseja pagar a taxa de 10% (sim/nao): ')
match taxa:
    case 'sim':
        valor = valor + valor * 10 / 100
        print(f'Valor a pagar: {valor}')
    case _:
        print(f'Valor a pagar: {valor}')0
'''