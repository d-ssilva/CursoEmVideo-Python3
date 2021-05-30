"""Crie um programa que leia dois valores e mostre um menu na tela:
1 - somar
2 - multiplicar
3 - maior
4 - novos números
5 - sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""
from time import sleep
v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
def menu():
    print('=' * 20)
    print('Digite para seguir com a opção desejada')
    print('[1] - soma')
    print('[2] - multiplicação')
    print('[3] - maior')
    print('[4] - Novos números')
    print('[5] - Sair do programa')
    print('='*20)
menu()
opc = int(input('Digite a opção aqui: '))

while opc != 5:
    if opc == 1:
        v3 = v1 + v2
        print(v3)
        menu()
        opc = int(input('Digite a opção aqui: '))
    elif opc == 2:
        v3 = v1 * v2
        print(v3)
        menu()
        opc = int(input('Digite a opção aqui: '))
    elif opc == 3:
        if v1 < v2:
            print('maior é {}'.format(v2))
            menu()
            opc = int(input('Digite a opção aqui: '))
        elif v1 > v2:
            print('maior é {}'.format(v1))
            menu()
            opc = int(input('Digite a opção aqui: '))
        else:
            print('Os números são iguais')
            menu()
            opc = int(input('Digite a opção aqui: '))
    elif opc == 4:
        v1 = int(input('Digite um valor: '))
        v2 = int(input('Digite outro valor: '))
        menu()
        opc = int(input('Digite a opção aqui: '))
    else:
        opc = int(input('Opção digitada errada, digite novamente: '))
print('Fechando programa...')
sleep(1)