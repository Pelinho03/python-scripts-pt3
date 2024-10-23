'''
105. Faz um programa que tenha uma função `notas()`, que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
- - Quantidade de notas.
- - A maior nota.
- - A menor nota.
- - A média da turma.
- - A situação (opcional).
'''


def notas(*n, sit=False):
    """
    --> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre as notas.
    """

    r = dict()  # Cria um dicionário para armazenar os resultados
    r['total'] = len(n)  # Total de notas inseridas
    r['maior'] = max(n)  # A maior nota
    r['menor'] = min(n)  # A menor nota
    r['média'] = sum(n) / len(n)  # Calcula a média das notas

    # Verifica se a situação deve ser calculada
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'  # Situação boa se a média for >= 7
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'  # Situação razoável se a média for >= 5
        else:
            r['situação'] = 'MAU'  # Situação mau se a média for < 5

    return r  # Retorna o dicionário com os resultados


# Programa principal
resp = notas(7.5, 8.5, 9.5, sit=True)  # Chama a função com algumas notas e situação
print(resp)  # Imprime o dicionário retornado
help(notas)  # Mostra a documentação da função
