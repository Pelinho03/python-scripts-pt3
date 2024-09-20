'''
084. Faz um programa que leia o nome e o peso de várias pessoas, guardando tudo numa lista. No final, mostra:
- A) Quantas pessoas foram registadas.
- B) Uma listagem com as pessoas mais pesadas.
- C) Uma listagem com as pessoas mais leves
'''
temp = []  # Lista temporária para armazenar o nome e o peso de uma pessoa
princ = []  # Lista principal que vai guardar todas as pessoas e seus pesos
mai = men = 0  # Variáveis para armazenar o maior e o menor peso

# Loop principal para registar várias pessoas
while True:
    # Adiciona o nome e o peso da pessoa à lista temporária
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    # Verifica se é o primeiro registo para definir o maior e menor peso
    if len(princ) == 0:
        mai = men = temp[1]  # Define o primeiro peso como maior e menor
    else:
        # Atualiza o maior peso se o peso atual for superior
        if temp[1] > mai:
            mai = temp[1]
        # Atualiza o menor peso se o peso atual for inferior
        if temp[1] < men:
            men = temp[1]

    # Adiciona uma cópia da lista 'temp' na lista principal 'princ'
    princ.append(temp[:])
    temp.clear()  # Limpa a lista temporária para o próximo registo

    # Pergunta ao utilizador se deseja continuar
    resp = str(input('Queres continuar? [S/N]')).strip().upper()[0]
    if resp in 'N':
        break  # Sai do loop se o utilizador responder 'N'

print('-=' * 30)
# Exibe quantas pessoas foram registadas
print(f'Ao todo, foram registados {len(princ)} pessoas.')

# Exibe o maior peso e as pessoas que possuem esse peso
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')  # Mostra o nome das pessoas com o maior peso
print()

# Exibe o menor peso e as pessoas que possuem esse peso
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')  # Mostra o nome das pessoas com o menor peso
print()
