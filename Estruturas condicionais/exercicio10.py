"""
Faça um algoritmo que solicite o salário fixo e o valor das vendas efetuadas pelo vendedor de uma
empresa. Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00
mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total."""

salarioFixo = float(input('Digite aqui o seu salario fixo:'))
valorVendas = float(input('Digite aqui o valor das vendas: '))

if valorVendas <= 1500:
    comissao = valorVendas * 0.03
    salarioTotal = salarioFixo + comissao
    print(f'O salário é {salarioTotal:.2f} Reais')
elif valorVendas > 1500:
    comissao = 1500 * 0.03
    comissao2 = (valorVendas - 1500) * 0.05
    comissaoTotal = comissao + comissao2
    salarioTotal = salarioFixo + comissaoTotal
    print(f'Salário Total: R$ {salarioTotal:.2f}')