conta_idade = 0
soma_idades = 0

while True <= 10:
    idade = int(input('Informe sua idade: '))
    if idade < 0:
        break
    soma_idades += idade
    conta_idade += 1
print(soma_idades)
if conta_idade > 0:
    media = soma_idades / conta_idade
    print(f'Média de idade das pessoas: {media:.2f}')
else:
    print('Nenhuma idade foi informada')