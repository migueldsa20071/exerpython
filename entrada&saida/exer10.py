num = int(input('Digite um número de três digitos aqui: '))

a = num // 100 # 1
resto = num % 100 # 36

b = resto // 10 #3
c = resto % 10 #6

print(f'Número invertido: {c}{b}{a}')  