'''
081. Cria um programa que vai ler vários números e colocá-los numa lista. Depois disso, mostra:
- A) Quantos números foram digitados.
- B) A lista de valores, ordenada de forma decrescente.
- C) Se o valor 5 foi digitado e se está ou não na lista.
'''
valores = []
while True:
    valores.append(int(input('Digita um valor: ')))
    resp = str(input('Queres continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-=' * 30)
print(f'Digitaste {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem descrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')
