'''
092. Cria um programa que leia o nome, o ano de nascimento e a carteira de trabalho de uma pessoa, registando também a idade num dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário também receberá o ano de contratação e o salário. Calcula e acrescenta, além da idade, com quantos anos a pessoa se vai reformar.
'''
from datetime import datetime

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: €'))
    dados['reforma'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
