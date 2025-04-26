n = int(input('Informe a quantidade de números: '))
contapares = 0
contaimpares = 0
somapares = 0
somaimpares = 0
cont = 1

while cont <= n:
    numero = int(input('Informe um numero:' ))
    if numero % 2 == 0:
        somapares += numero
        contapares += 1
    else:
        somaimpares += numero
        contaimpares += 1
    cont += 1
if contapares > 0:
    print(f'A Médias dos pares: {somapares / contapares}')
else:
    print('Não foi digitado nenhum número par')

if contaimpares > 0:
    print(f'A Médias dos pares: {somaimpares / contaimpares}')
else:
    print('Não foi digitado nenhum número ímpar')
