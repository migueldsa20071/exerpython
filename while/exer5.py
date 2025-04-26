n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))

while n1 == n2:
    print('Digite os números novamentes (diferentes 1 do 2)')
    n1 = int(input('Informe o primeiro número: '))
    n2 = int(input('Informe o segundo número: '))
if n1 != n2:
 print(f'{n1 + n2} Essa é a soma de {n1} com {n2}')