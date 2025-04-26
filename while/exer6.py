
num = int(input(f'Digite um numero'))
numM = num

cont = 1
while cont <= 9:
    num = int(input(f'Digite um numero'))
    if num < numM:
        numM = num
    cont +=1

print(f'Menor número: {numM}')
