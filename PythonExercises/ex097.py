'''
097. Faz um programa que tenha uma função chamada escreva(), que recebe um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
'''
def escreva(txt):
    # Calcula a dimensão da moldura, somando 4 para adicionar espaços laterais
    dim = len(txt) + 4
    # Imprime a linha superior da moldura
    print('~' * dim)
    # Imprime o texto com 2 espaços de margem de cada lado
    print(f'  {txt}  ')
    # Imprime a linha inferior da moldura
    print('~' * dim)


# Pede ao utilizador para inserir uma frase
escreva(str(input('Digita uma frase: ')).strip())
