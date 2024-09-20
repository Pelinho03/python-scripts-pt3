'''
089. Cria um programa que leia o nome e duas notas de vários alunos e guarde tudo numa lista composta. No final, mostra um boletim contendo a média de cada aluno e permite que o utilizador possa mostrar as notas de cada aluno individualmente.
'''
alunos = []  # Lista composta para armazenar os alunos e suas notas

# Loop principal para adicionar alunos
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    # Adiciona o nome e as notas à lista 'alunos' como uma sublista
    alunos.append([nome, nota1, nota2])

    # Pergunta ao utilizador se deseja continuar a adicionar alunos
    escolha = str(input('Queres continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break  # Sai do loop se o utilizador digitar 'N'

# Mostrar boletim com as médias
print('=' * 30)
print('{:<10} {:<10} {:>10}'.format('Nº', 'Nome', 'Média'))
print('=' * 30)

# Exibir os alunos e suas médias
for i, aluno in enumerate(alunos):
    nome = aluno[0]
    media = (aluno[1] + aluno[2]) / 2  # Calcula a média das duas notas
    print(f'{i:<10} {nome:<10} {media:>10.1f}')

# Permitir que o utilizador veja as notas individuais de cada aluno
while True:
    print('=' * 30)
    opcao = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))

    if opcao == 999:
        print('A encerrar o programa...')
        break  # Sai do programa se o utilizador digitar 999

    if opcao < len(alunos):
        # Mostra as notas do aluno escolhido
        nome = alunos[opcao][0]
        nota1 = alunos[opcao][1]
        nota2 = alunos[opcao][2]
        print(f'Notas de {nome}: Nota 1 = {nota1}, Nota 2 = {nota2}')
    else:
        print('Aluno não encontrado, tenta outra vez.')
