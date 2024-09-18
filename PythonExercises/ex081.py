'''
081. Cria um programa que vai ler vários números e colocá-los numa lista. Depois disso, mostra:
- A) Quantos números foram digitados.
- B) A lista de valores, ordenada de forma decrescente.
- C) Se o valor 5 foi digitado e se está ou não na lista.
'''
# Inicializa uma lista vazia para armazenar os números.
valores = []

# Pede ao utilizador quantos números ele deseja inserir.
vezes = int(input('Quantos números queres inserir? '))

# Loop para ler os números e adicionar à lista.
for i in range(vezes):
    num = int(input(f'Insere o {i + 1}º número: '))
    valores.append(num)

# A) Mostra quantos números foram digitados.
print(f'Foram digitados {len(valores)} números.')

# B) Mostra a lista de valores, ordenada de forma decrescente.
print(f'Lista de valores em ordem decrescente: {sorted(valores, reverse=True)}')

# C) Verifica se o valor 5 foi digitado e mostra a mensagem correspondente.
if 5 in valores:
    print('O valor 5 foi digitado.')
else:
    print('O valor 5 não foi digitado.')

