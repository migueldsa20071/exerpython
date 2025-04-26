"""
Solicite ao usuário três números e exibe apenas o menor deles,
ou uma mensagem informando que os números são iguais.
"""


num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num3 > num1 and num2 > num1:
    print(f'O menor número é o {num1}')
elif num3 > num2 and num1 > num2:
    print(f'O menor número é o {num2}')
elif num1 > num3 and num2 > num3:
    print(f'O menor número é o {num3}')
else:
    print('Os três números são iguais')