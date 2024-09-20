pessoa = {'nome': 'Paulo', 'sexo': 'M', 'idade': 25}
print(pessoa['idade'])  # Mostra a idade da pessoa
print(pessoa['nome'])  # Mostra o nome da pessoa
print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos.')  # Formata uma frase com o nome e idade

# Mostra as chaves, valores e itens do dicionário
print(pessoa.keys())  # Chaves do dicionário (nome, sexo, idade)
print(pessoa.values())  # Valores do dicionário (Paulo, M, 25)
print(pessoa.items())  # Itens (chave, valor) do dicionário

# Iteração pelas chaves
for k in pessoa.keys():
    print(k)

# Iteração pelos valores
for v in pessoa.values():
    print(v)

# Iteração pelos itens (chave e valor)
for k, v in pessoa.items():
    print(f'{k} = {v}')

# Alteração e remoção de valores
pessoa['nome'] = 'Leandro'  # Muda o nome para Leandro
pessoa['peso'] = 80.5  # Adiciona o peso ao dicionário
del pessoa['sexo']  # Remove o campo sexo

# Mostra o dicionário atualizado
for k, v in pessoa.items():
    print(f'{k} = {v}')
