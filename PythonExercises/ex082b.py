'''
082.  Cria um programa que vai ler vários números e colocá-los numa lista. Depois disso, cria duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respetivamente. No final, mostra o conteúdo das três listas geradas.
'''
num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digita um número ')))
    resp = str(input('Queres continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}'
      f'\nA lista de pares é {pares}'
      f'\nA lista de ímpares é {impares}')
