'''
Escreva um programa que solicite um número inteiro maior do que zero e menor do que 1000 e exiba a soma de todos os seus
algarismos. Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se o número lido não for maior
do que zero e menor que 1000, o programa terminará com a mensagem "Número inválido".
'''

 #for casa in str(num) usei para transformar os números em string
# usei o sum para somar cada valor

num = int(input('Digite um número inteiro maior que 0 e menor que 1000: '))

if num > 0 and num <= 1000:
    soma = sum(int(casa) for casa in str(num))
    print(f'A soma dos algarismos de {num} é {soma}')
else: 
    print('Esse número é inválido')





    