'''
101. Cria um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
'''
from datetime import date  # Importar o módulo date para obter a data atual

# Obtém o ano e mês atuais
ano_atual = date.today().year
mes_atual = date.today().month


def voto(ano_nascimento, mes_nascimento):
    """
    Função que determina se o voto é NEGADO, OPCIONAL ou OBRIGATÓRIO
    com base no ano e mês de nascimento do utilizador.

    :param ano_nascimento: Ano de nascimento do utilizador (int)
    :param mes_nascimento: Mês de nascimento do utilizador (int)
    :return: Uma string indicando se o voto é NEGADO, OPCIONAL ou OBRIGATÓRIO.
    """

    # Calcula a idade baseando-se no ano atual e no ano de nascimento
    idade = ano_atual - ano_nascimento

    # Verifica se a pessoa ainda não fez anos este ano
    # Se o mês de nascimento ainda não chegou, a idade é ajustada
    if mes_nascimento > mes_atual:
        idade -= 1

    # Determina o status do voto com base na idade
    if idade < 16:  # Menores de 16 não podem votar
        return f'Tens {idade} anos e o teu voto foi NEGADO.'
    elif 16 <= idade < 18 or idade >= 70:  # Entre 16 e 18 ou maiores de 70 têm voto opcional
        return f'Tens {idade} anos e o teu voto é OPCIONAL.'
    else:  # Pessoas entre 18 e 70 têm voto obrigatório
        return f'Tens {idade} anos e o teu voto é OBRIGATÓRIO.'


# Pede os dados de entrada ao utilizador
ano_nasc = int(input('Digita o teu ano de nascimento: '))
mes_nasc = int(input('Digita o teu mês de nascimento (1-12): '))

# Chama a função 'voto' e imprime o resultado
resultado = voto(ano_nasc, mes_nasc)
print(resultado)
