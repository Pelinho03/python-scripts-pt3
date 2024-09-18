'''
080. Cria um programa onde o utilizador possa digitar cinco valores numéricos e registá-los numa lista, já na posição correta de inserção (sem usar o sort()). No final, mostra a lista ordenada no ecrã.
'''
lista = list()
for c in range(5):
    n = int(input('Digita um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
