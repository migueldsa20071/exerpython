soma = 0
while True:
    numero = int(input('Numero: '))
    if numero == 0:
        break
    soma += numero
print(f'Somatório: {soma}')