numero = int(input('Informe um número inteiro: '))

fatorial = 1
for n in range(numero, 0, -1):
    fatorial = fatorial * n

print(f'Fatorial de {numero} é {fatorial}')