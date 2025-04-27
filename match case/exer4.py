'''
Faça um algoritmo que solicite o código da palestra de um evento e exiba o local em que ela será realizada,
conforme a tabela
'''

sol = int(input('Informe o código do evento: '))

match sol:
    case 1:
        print('Sera realizada no auditório 1')
    case 2:
        print('Sera realizada no auditório 2')
    case 3: 
        print('Sera realizada no auditório 3')
    case 4:
        print('Sera realizada no auditório principal')
    case _ :
        print('Opção inválida')