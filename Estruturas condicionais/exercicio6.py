a = int(input('Digite que horas são agora: '))
b = int(input('Digite os minutos: '))

if a >= 0 and 24 > a and b >= 0 and b < 60 :
 print(f'Agora são {a} e {b} ')
else:
    print('Horário inválido')
