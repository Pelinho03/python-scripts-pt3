'''
096. Faz um programa que tenha uma função chamada área(), que recebe as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''
def area(l, c):
    areaterreno = l * c
    print(f'\nA área do terreno retangular de {l}m de largura e {c}m de comprimento é {areaterreno}m².')


print('-' * 30)
print('{:^30}'.format('TERRENO'))
print('-' * 30)
# Entrada de dados
largura = float(input('Digite a largura do terreno (em metros): '))
comprimento = float(input('Digite o comprimento do terreno (em metros): '))

# Chamada da função
area(largura, comprimento)
