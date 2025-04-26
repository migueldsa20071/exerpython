n = int(input('Informe 10 Números:'))
maior = n
menor = n

for num in range(9):
    n = int(input('Informe 10 Números:'))
    if n > maior:
        maior = n
    if n < menor:
        menor = n


print(f'Esse é o maior {maior}')
print(f'Esse é o menor {menor}')
