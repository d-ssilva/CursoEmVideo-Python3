"""Adaptação do DESAFIO 064 - Tratando vários valores
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag"""
cont = tot = 0
flag = 999
print('=-'*10, '|', 'Tratando valores', '|', '-='*10)
num = int(input('Digite um número -> '))
while True:
    cont += 1
    tot += num
    num = int(input('Continue digitando... -> '))
    if num == 999:
        break
print('-='*31)
print('Você digitou {} vezes, a soma de todos os números digitados é {}'.format(cont, tot))
