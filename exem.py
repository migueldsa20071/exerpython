def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media


def verificar_status(media):
    if media < 6:
        return '\033[31mReprovado\033[0m'
    elif 6 <= media < 7:
        return '\033[33mRegular\033[0m'
    elif 7 <= media < 9:
        return '\033[32mBom\033[0m'
    elif 9 <= media <= 10:
        return '\033[33mMuito Bom\033[0m'


notas = []
for i in range(5):
    nota = float(input(f'Digite a nota {i+1}: '))
    notas.append(nota)


media = calcular_media(notas)
status = verificar_status(media)

print(f'Média: {media:.2f}')
print(f'Status: {status}')

