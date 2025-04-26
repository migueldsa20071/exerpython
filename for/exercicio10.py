qtd_alunos = int(input('Qtd de alunos: '))
qtd_notas = int(input('qtd de notas: '))

for a in range(qtd_alunos):


     for n in range(qtd_notas):
         nota = float(input('Nota: '))
         soma += nota
         media: soma / qtd_notas
         print(f'Média: {media}')