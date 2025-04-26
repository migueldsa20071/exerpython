nome = input('Digite seu nome: ')
qtdCarros = int(input('Digite quantos carros você vendeu: '))
valorTotal = float(input('Digite o valor total de suas vendas:'))

salario = 2500 + (200 * qtdCarros) + (valorTotal/100 * 2)

print(f'O salario do vendedor {nome}, é {salario:.2f}')