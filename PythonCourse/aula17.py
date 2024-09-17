num = [2, 5, 9, 1]
num[2] = 3
print(num)

#num[4]=7 erro
num.append(7)

num.sort()
print(num)

num.sort(reverse=True)
print(num)

num.insert(2,0)
print(num)

num.pop(2)

num.insert(2,2)
print(num)

if 4 in num:
    num.remove(2)
else:
    print('Não encontrei o número 4.')

print(num)
print(f'Esta lista tem {len(num)} elementos.')