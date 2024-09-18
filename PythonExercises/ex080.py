'''
080. Cria um programa onde o utilizador possa digitar cinco valores numéricos e registá-los numa lista, já na posição correta de inserção (sem usar o sort()). No final, mostra a lista ordenada no ecrã.
'''
# Inicializa uma lista vazia para armazenar os valores.
valores = []

for i in range(5):
    num = int(input(f'Insere o {i + 1}º número: '))

    # Verifica onde o número deve ser inserido na lista.
    if len(valores) == 0 or num >= valores[-1]:
        # Se a lista estiver vazia ou o número é maior ou igual ao último valor da lista, adiciona ao final.
        valores.append(num)
    else:
        # Encontra a posição correta para inserir o número mantendo a ordem crescente.
        pos = 0
        while pos < len(valores) and num > valores[pos]:
            pos += 1
        # Insere o número na posição encontrada.
        valores.insert(pos, num)

# Mostra a lista ordenada no ecrã.
print(f'Lista ordenada: {valores}')
