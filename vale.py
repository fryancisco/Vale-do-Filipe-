from operator import truediv
def soma(sb):
    if sb > vale:
        print(f'O funcionario pode pegar {vale} de vale')
    else:
        print(f'O funcionario não pode pegar {vale} de vale')

while True:
    cart = str(input('O funcionario é carteira assinada? [S/N] ')).upper()
    dev = float(input('Quanto o funcionario esta devendo? '))
    vale = float(input('Qaunto de vale ele quer? '))
    dtrab = float(input('Quantos dias o funcionario trabalhou? '))

    if cart == 'S':
        s = dtrab * 37.5
        sb = s - dev
        soma(sb)
    else:
        s = dtrab * 36.66
        sb = s - dev
        soma(sb)

    cont = str(input('Voce deseja fazer outra analise? [S/N] ')).upper()
    if cont == 'N':
        break
