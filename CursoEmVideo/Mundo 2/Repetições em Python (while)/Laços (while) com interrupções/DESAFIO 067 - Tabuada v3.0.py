"""Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo"""
print('=-'*10, '|', 'TABUADA v3.0', '|', '-='*10)
n = int(input('Digite um número do qual deseje ver sua tabuada: '))
cont = 1
while True:
    print(f'{n} x {cont} = {n*cont}')
    cont += 1
    if cont == 11:
        print('=-'*31)
        n = int(input('Deseja ver qual número agora? (um número negativo, fecha o app)'
                      '\nDigite aqui -> '))
        cont = 0
        print('=-'*30)
        if n < 0:
            break
print('FIM DO PROGRAMA!')
