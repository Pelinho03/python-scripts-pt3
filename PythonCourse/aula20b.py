def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')


def contador2(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

contador2(2, 1, 7)
contador2(8, 0)
contador2(4, 4, 7, 6, 2)
