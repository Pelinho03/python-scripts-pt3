valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digita um valor: ')))

for c, e in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {e}!')
print('Cheguei ao final da lista.')
