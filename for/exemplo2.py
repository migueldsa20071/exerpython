#Solicitar a idade de N pessoas e calcular a média das idades

soma = 0

n = int(input('Quantas pessoas são no total?: '))
for cont in range(n):
    idade = int(input('Difite a idade: '))
    soma += idade

media = soma / n
print(f'Média das idades: {media:.2f}')
