""" Funções ou rotinas e como utilizar funções em Python. Funções são trechos de código que
    podem ser executados em momentos diferentes de nossos códigos em Python.
    Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos."""
def mensagem(msg):
    print('='*40)
    print(f'{msg:^40}')
    print('=' * 40)

mensagem('SISTEMA DE ALUNOS')
mensagem('É o bicho mlk doido')