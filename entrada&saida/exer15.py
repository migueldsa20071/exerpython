votosEmBranco = 35
votosNulos = 10
votosVálidos = 60

votosTotais = votosVálidos + votosNulos + votosEmBranco

percVotoEmBranco = (votosTotais * votosEmBranco) / votosTotais
percVotosNulos =votosTotais/votosNulos

print(f'{percVotoEmBranco:.2f}')
print(f'{percVotosNulos:.2f}')