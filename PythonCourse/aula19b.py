portugal = []
distrito1 = {'distrito': 'Lisboa', 'sigla': 'LX'}
distrito2 = {'distrito': 'Porto', 'sigla': 'PO'}

# Adiciona os dicionários à lista
portugal.append(distrito1)
portugal.append(distrito2)

# Mostra os dicionários individuais e a lista completa
print(distrito1)  # {'distrito': 'Lisboa', 'sigla': 'LX'}
print(distrito2)  # {'distrito': 'Porto', 'sigla': 'PO'}
print(portugal)  # [{'distrito': 'Lisboa', 'sigla': 'LX'}, {'distrito': 'Porto', 'sigla': 'PO'}]

# Acessa elementos específicos
print(portugal[0])  # {'distrito': 'Lisboa', 'sigla': 'LX'}
print(portugal[1]['sigla'])  # PO (sigla do Porto)
