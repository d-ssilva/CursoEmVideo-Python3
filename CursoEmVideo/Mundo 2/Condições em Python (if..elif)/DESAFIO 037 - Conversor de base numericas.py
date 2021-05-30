'''
Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de
conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''

# inserção de informações
usernum = int(input('Digite um número qualquer: '))
print('{}, você desaja usar qual base de converção?\n'
      '[1]-Para binário\n'
      '[2]-Para octal\n'
      '[3]-Para hexadecimal'.format(usernum))
useroption = int(input('Digite a opção desejada: '))

# estrutura condicional aninhada
if useroption == 1:
    print('A conversão de {} para base BINÁRIA é {}.'.format(usernum, bin(usernum)[2:]))
elif useroption == 2:
    print('A conversão de {} para base OCTAL, é {}.'.format(usernum, oct(usernum)[2:]))
elif useroption == 3:
    print('A conversão de {} para base HEXADECIMAL é {}'.format(usernum, hex(usernum)[2:]))
else:
    print('Valor inválido.\nTente novamente.')

