pessoas = [['Paulo', 24], ['Rita', 25], ['Maria', 12], ['João', 32]]
print(pessoas)
print(pessoas[0])
print(pessoas[0][0])
print(pessoas[2][1])

for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')
