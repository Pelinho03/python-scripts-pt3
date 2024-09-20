'''
089. Cria um programa que leia o nome e duas notas de vários alunos e guarde tudo numa lista composta. No final, mostra um boletim contendo a média de cada aluno e permite que o utilizador possa mostrar as notas de cada aluno individualmente.
'''
ficha = list()  # Lista composta que armazenará os dados de cada aluno (nome, notas e média)

# Loop principal para o registo de alunos e suas notas
while True:
    nome = str(input('Nome: '))  # Recebe o nome do aluno
    nota1 = float(input('Nota 1: '))  # Recebe a primeira nota do aluno
    nota2 = float(input('Nota 2: '))  # Recebe a segunda nota do aluno
    media = (nota1 + nota2) / 2  # Calcula a média das duas notas
    ficha.append([nome, [nota1, nota2], media])  # Adiciona uma lista composta por nome, notas e média à ficha
    resp = str(input('Queres continuar? [S/N] '))  # Pergunta se o utilizador quer continuar
    if resp in 'Nn':  # Se a resposta for 'N' ou 'n', o loop termina
        break

# Cabeçalho da tabela com os alunos e suas médias
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')  # Exibe os títulos das colunas (número, nome e média)
print('_' * 26)

# Exibe o índice, nome e média de cada aluno
for i, a in enumerate(ficha):  # Loop para enumerar cada aluno na ficha
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')  # Exibe o número do aluno, o nome e a média formatada com uma casa decimal

# Loop para consultar as notas individuais de um aluno específico
while True:
    print('_' * 35)
    opc = int(input('Mostrar notas de que aluno? (999 para interromper.) '))  # Pergunta qual aluno mostrar as notas
    if opc == 999:  # Se o utilizador digitar 999, o programa termina
        print('A ENCERRAR...')
        break
    if opc <= len(ficha) - 1:  # Verifica se o número escolhido é válido (dentro da lista de alunos)
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')  # Mostra as notas do aluno escolhido

print('<<< VOLTE SEMPRE >>>')  # Mensagem de encerramento do programa
