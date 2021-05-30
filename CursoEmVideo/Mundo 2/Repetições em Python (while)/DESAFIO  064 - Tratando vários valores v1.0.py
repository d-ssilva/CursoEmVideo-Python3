"""Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag)"""
cont = tot = 0
flag = 999
print('=-'*10, '|', 'Tratando valores', '|', '-='*10)
num = int(input('Digite um número -> '))
if num != flag:
    while num != flag:
        tot += num
        cont += 1
        num = int(input('Continue digitando... -> '))
elif num == flag:
    if tot <= 0:
        tot = tot + tot
print('-='*31)
print('Você digitou {} vezes, a soma de todos os números digitados é {}'.format(cont, tot))
