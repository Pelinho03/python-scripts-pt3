'''
077.  Criar um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, deve mostrar, para cada palavra, quais são as vogais.
'''
# Tupla com várias palavras (sem acentos)
palavras = ('computador', 'mesa', 'cadeira', 'programacao', 'python', 'teclado', 'monitor')

# Percorrer cada palavra na tupla
for palavra in palavras:
    # Exibir a palavra
    print(f'\nNa palavra "{palavra.upper()}" temos as vogais: ', end='')

    # Verificar cada letra na palavra
    for letra in palavra:
        # Se a letra for uma vogal, exibir
        if letra in 'aeiou':
            print(letra, end=' ')
