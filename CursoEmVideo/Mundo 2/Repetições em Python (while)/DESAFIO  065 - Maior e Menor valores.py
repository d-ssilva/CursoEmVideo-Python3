"""Crie um programa que leia vários números inteiros pelo teclado.
 - No final da execução, mostre a MÉDIA entre todos os valroes
 e qual foi o maior e o menor valores lidos.
 - O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""
# VARIÁVEIS
num = 0
cont = 0
resp = 'S'
tot = 0
maior = 0
menor = 0

print('=-'*10, '|', 'Maior e Menor Valores', '|', '-='*10)
# INSERÇÃO DE VALORES
while resp == 'S':
    num = int(input('Digite um número (exceto 0) -> '))
    if cont == 0:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    if num < menor:
        menor = num
    cont += 1
    tot += num
    resp = str(input('Quer continuar digitando? [S/N] -> ')).upper()[0]  # VERIFICAÇÃO DE FLAG

print('Você digitou {} vezes, a soma dos valores é {} e a média entre os valores digitados é é {:.2f}\n'
      'O maior valor digitado foi {}\n'
      'O menor valor digitado foi {}'.format(cont, tot, tot / cont, maior, menor))
