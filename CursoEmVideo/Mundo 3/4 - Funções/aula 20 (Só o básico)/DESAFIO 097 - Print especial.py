"""Faça um programa que tenha a função chamada escreva(), que receba um texto qualquer como parâmetro e
   mostre uma mensagem com tamanhã adaptável.
   Ex:
   escreva("Olá, Mundo!")
   Saída
   ==============
   Olá, Mundo!
   =============="""
def escreva(msg):
    print('=' * 40)
    print(f'{msg:^40}')
    print('=' * 40)


escreva(input('Escreva uma mensagem: ').capitalize())
