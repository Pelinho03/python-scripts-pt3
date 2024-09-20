distrito = dict()
portugal = list()

# Registo de 3 distritos (podes alterar o número de distritos)
for c in range(3):
    distrito['distrito'] = str(input('Distrito: '))  # Nome do distrito
    distrito['sigla'] = str(input('Sigla do Distrito: '))  # Sigla do distrito
    portugal.append(distrito.copy())  # Adiciona uma cópia do dicionário à lista

# Mostra cada distrito com as suas chaves e valores
for d in portugal:
    for k, v in d.items():
        print(f'O campo {k} tem o valor {v}.')

# Mostra apenas os valores (nomes e siglas dos distritos)
for d in portugal:
    for v in d.values():
        print(v, end=' ')
    print()
