'''
Solicite um número ao usuário. se o número for positivo, calcule a metade deses número
Se o número for negativo, mostre o numero ao quadrado.'''



num = float(input('Digite algum número: '))

if num > 0:
    num = num/2
    print(f'Essa é a metade do número que você escolheu: {num}')
elif num < 0:
   num = num **2
   print(f'Esse é o quadrado do número que você escolheu: {num}')