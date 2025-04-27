qtd_alunos = int(input('Qtd de alunos: '))
qtd_notas = int(input('Qtd de notas: '))

for a in range(qtd_alunos):
    soma = 0  
    for n in range(qtd_notas):
        nota = float(input('Nota: '))
        soma += nota
    media = soma / qtd_notas  
    print(f'Média do aluno {a + 1}: {media:.2f}')
