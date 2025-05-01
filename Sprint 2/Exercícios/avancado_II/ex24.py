import csv

with open('estudantes.csv', 'r') as planilha:
    arquivo = csv.reader(planilha)
    lista_alunos = sorted(list(arquivo), key=lambda x: x[0])

for aluno in lista_alunos:
    nome = aluno[0]
    notas = list(map(float, aluno[1:]))
    top_3_notas = sorted(notas, reverse=True)[:3]
    media = round(sum(top_3_notas) / 3, 2)
    notas_mod = [int(nota) if nota.is_integer() else round(nota, 1) for nota in top_3_notas]

    print(f"Nome: {nome} Notas: {notas_mod} Média: {media}")
