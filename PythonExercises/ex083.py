'''
083. Cria um programa onde o utilizador digite uma expressão qualquer que utilize parênteses. O programa deve analisar se a expressão tem os parênteses abertos e fechados na ordem correta.
'''
def verificar_expressao(expressao):
    # Cria uma pilha para armazenar os parênteses abertos
    pilha = []

    # Dicionário para mapear parênteses de fechamento para os de abertura correspondentes
    pares = {')': '(', ']': '[', '}': '{'}

    # Percorre cada caractere da expressão
    for char in expressao:
        # Se o caractere é um parêntese de abertura, adiciona à pilha
        if char in pares.values():
            pilha.append(char)
        # Se o caractere é um parêntese de fechamento
        elif char in pares.keys():
            # Verifica se a pilha está vazia ou se o parêntese de fechamento não corresponde ao parêntese de abertura no topo da pilha
            if not pilha or pilha[-1] != pares[char]:
                return False
            # Remove o parêntese de abertura correspondente da pilha
            pilha.pop()

    # Se a pilha estiver vazia, todos os parênteses estão balanceados
    return len(pilha) == 0


# Leitura da expressão do usuário
expressao = input("Digite uma expressão com parênteses: ")

# Verifica se a expressão está balanceada e imprime o resultado
if verificar_expressao(expressao):
    print("A expressão está com os parênteses corretamente balanceados.")
else:
    print("A expressão não está com os parênteses corretamente balanceados.")
