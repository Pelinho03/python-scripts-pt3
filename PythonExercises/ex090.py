'''
090. Faz um programa que leia o nome e a média de um aluno, guardando também a situação num dicionário. No final, mostra o conteúdo da estrutura no ecrã.
'''
aluno = dict()  # Dicionário para armazenar dados do aluno
escola = list()  # Lista para armazenar os dicionários de todos os alunos

while True:
    aluno['nome'] = str(input('Nome: '))  # Pede o nome do aluno
    aluno['media'] = float(input('Média: '))  # Pede a média do aluno

    # Determina a situação com base na média
    if aluno['media'] < 10:
        aluno['situação'] = 'Reprovado'
    else:
        aluno['situação'] = 'Aprovado'

    escola.append(aluno.copy())  # Adiciona uma cópia do dicionário à lista

    # Pergunta se o utilizador quer continuar
    resp = str(input('Queres continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        print('A calcular resultados...')
        break  # Sai do ciclo se a resposta for "N"

# Mostra os dados de todos os alunos armazenados
print('-=' * 30)
for aluno in escola:
    print(f"Nome: {aluno['nome']}, Média: {aluno['media']}, Situação: {aluno['situação']}")
print('-=' * 30)
