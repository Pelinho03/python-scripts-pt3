'''
072. Criar um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. O programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''
# Tupla com números por extenso
contagem = (
    'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
    'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
)

while True:
    # Leitura do número do usuário
    num = int(input('Digite um número entre 0 e 20 (ou -1 para sair): '))

    # Verifica se o usuário deseja sair
    if num == -1:
        print('Programa terminado.')
        break
    # Verifica se o número está fora do intervalo permitido
    elif num < 0 or num > 20:
        print('VALOR ERRADO! Tente novamente.')
    else:
        # Mostra o número por extenso
        print(f'O valor digitado é {num} que corresponde a {contagem[num]}.')
