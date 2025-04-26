#Solicitar 10 npumeros e ver quantos são pares
cont = 1
conta_P = 0
conta_I = 0
conta_N = 0 # Contadores
while cont <= 10:
    numero = int(input('Número: '))
    if numero % 2 == 0:
        conta_P += 1    # conta os  números pares
    else:
        conta_I +=1
    if numero < 0:
        conta_N += 1
    cont +=1

print(f'Quantidade de numeros pares: {conta_P}')
print(f'Quantidade de numeros ímpares: {conta_I}')
print(f'Quantidade de numeros negativos: {conta_N}')