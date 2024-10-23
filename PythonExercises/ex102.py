def fatorial(n, show=False):
    """
    --> Calcular o Fatorial de um número.
    :param n: Número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1  # Inicializa a variável para armazenar o resultado do fatorial
    # Ciclo para calcular o fatorial de n até 1
    for c in range(n, 0, -1):
        if show:  # Se o parâmetro 'show' for True, exibe o processo de cálculo
            print(c, end='')  # Mostra o valor atual de 'c'
            if c > 1:
                print(' x ', end='')  # Se não for o último número, mostra o símbolo 'x'
            else:
                print(' = ', end='')  # No último número, mostra o símbolo '='
        f *= c  # Multiplica o valor atual de 'f' pelo valor de 'c'
    return f  # Retorna o resultado final do fatorial


# Exemplo de uso da função com o parâmetro 'show' como True para mostrar o processo de cálculo
print(fatorial(5, show=True))

# Exibe a documentação da função usando a função built-in help
help(fatorial)
