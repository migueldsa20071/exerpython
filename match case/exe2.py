valorToal = float(input('Digite o valor total da compra: '))
voce = input('Digite "F" se você é um funcionário, "V" cliente vip ou um cliente comum "C": ')

match voce:
    case "F" | "f":
        pagar = valorToal/100 * 90
        print(f'Você é um funcionário e ira pagar somente {pagar:.2f}')
    case "V" | "v":
        pagar = valorToal/100 * 95
        print(f'Você é um cliente vip e ira pagar somente {pagar:.2f}')
    case "C" | "c":
        pagar = valorToal
        print(F'Você é um cliente comum e ira pagar o valor normal {pagar:.2f}')
    case _:
        print('Essa opção é inválida')