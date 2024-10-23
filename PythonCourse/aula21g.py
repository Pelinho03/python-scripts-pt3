def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


f1 = fatorial(5)
f2 = fatorial(3)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

num = int(input('Digita um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
