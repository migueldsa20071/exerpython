"""
Faça um programa que solicite 2 notas de um aluno, verifique se as notas são válidas e exiba a média destas notas 
na tela. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0. Caso a nota não possua
um válor valido, este fato deve ser informado ao usuário e o programa finalizado.
."""

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

if nota1>=0 and nota1 <= 10 and nota2 >=0 and nota2 <=10:
    media = (nota1 + nota2) /2
    print(f'A média das suas notas é {media:.2f}')
else: 
    print('Alguma nota informada esta inválida')