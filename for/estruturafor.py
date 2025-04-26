#Quando Não sabemos a quantia de repetições iremos fazer, usaremos o while e não o for

#usamos range(valor)

#3 formas de usar o range
#range(stop) onde termina
#range(start, stop) onde começa e onde termina
#range(start, stop, step) onde começa, onde termina e de quanto em quanto

for numero in range(0, 10, 2): #começa no 1 e ira ir de 2 em 2 até dar o 9
    print(numero)

# for numero ir range (10, 0, -2) sequencia decrescentes, valor diminui
#só pode usar valores inteiros

#se sabemos a quantia de repetiçoes o for é mais simples de usar