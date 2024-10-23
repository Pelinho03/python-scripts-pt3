'''
104. Cria um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
    Ex: n = leiaInt('Digite um número: ')
'''


def leiaInt(msg):
    # Inicializa variáveis de controle
    ok = False
    valor = 0
    while True:
        # Recebe a entrada do utilizador
        n = str(input(msg))
        # Verifica se o valor é numérico
        if n.isnumeric():
            valor = int(n)  # Converte a string para inteiro
            ok = True
        else:
            # Mostra mensagem de erro se o valor não for numérico
            print('\033[0;31mERRO! Digita um número inteiro válido. \033[m')
        if ok:
            break  # Sai do loop se o valor for válido
    return valor  # Retorna o valor numérico


# Programa principal
n = leiaInt('Digita um número: ')  # Chama a função para ler um número
print(f'Digitaste o número {n}.')  # Mostra o número inserido
