teste = list()
teste.append('Paulo')
teste.append(24)
pessoas = list()
pessoas.append(teste[:])
teste[0] = 'Rita'
teste[1] = 22
pessoas.append(teste[:])
print(pessoas)
