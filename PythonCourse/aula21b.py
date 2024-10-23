def contador(i, f, p):
    '''
    -->Fazer um contagem e mostrar no ecrã.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    '''
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

# contador(0, 100, 10)
help(contador)