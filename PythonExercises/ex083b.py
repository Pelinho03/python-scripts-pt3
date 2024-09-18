'''
083. Cria um programa onde o utilizador digite uma expressão qualquer que utilize parênteses. O programa deve analisar se a expressão tem os parênteses abertos e fechados na ordem correta.
'''
expr = str(input('Digita a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A tua expressão está válida!')
else:
    print('A tua expressão está errada!')
