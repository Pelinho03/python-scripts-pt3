valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end='')

for c, e in enumerate(valores):
    print(f'\nNa posição {c} encontrei o valor {e}!')
print('Cheguei ao final da lista.')
