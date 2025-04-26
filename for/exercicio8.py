numero = int(input('Numero: '))

conta_divisores = 0
for n in range(1, numero+1):
    if numero % n == 0:
        conta_divisores += 1

if conta_divisores ==2:
    print(f'O numero {numero} é primo')
else:
    print(f'O numero {numero} não é primo')