num1 = int(input('Digite um número: '))
selecione = int(input('Selecione o tipo de cálculo que deve ser realizado \n 1- O dobro \n 2- A metade \n 3- 10% do número: '))

match selecione:
    case 1:
        num1 = num1 *2
        print(f'{num1} Esse é o dobro do número que você escolheu')
    case 2:
        num1 = num1 / 2
        print(f'{num1} Essa á a metade do número que você escolheu')
    case 3:
        num1 = num1* 0.10
        print(f'{num1} Esse é 10% do número que você escolheu')
    case _:
        print('Opção inválida')