"""
Faça um algoritmo que solicita ao usuário três valores correspondentes aos lados de um triângulo.
Informe se o triângulo é equilátero (possui 3 lados iguais), isósceles (possui dois lados iguais)
ou escaleno (não possui lados iguais).
"""

num1 = float(input('Digite o primeiro lado do triângulo: '))
num2 = float(input('Digite o segundo lado do triângulo: '))
num3 = float(input('Digite o terceiro lado do triângulo: '))

if(num1 == num2 and num1 == num3):
    print('Esse triangulo é equiláterio')
elif (num1 ==num2 or num2 ==num3 or num1 ==num3):
    print('É um triangulo isósceles')
else:
    print('é um triangulo escaleno')
