def lin():
    print('-' * 30)


def titulo(txt):
    print('-' * 30)
    print('{:^30}'.format(txt))
    print('-' * 30)


# sem def
print('-' * 30)
print('{:^30}'.format('PAULO GUIMARÃES'))
print('-' * 30)

# com def de linha
lin()
print('{:^30}'.format('PARENDER PYTHON'))
lin()

# com def de bloco de mensagem completo
titulo('OLÁ, MUNDO!')
