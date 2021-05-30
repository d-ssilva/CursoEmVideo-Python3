numero = soma = 0
while True:  # "True" faz com que o laço repita tudo pra sempre, até que o comando "break" seja identificado
    numero = int(input('Digite um número: '))
    soma += numero
print('A soma vale {}'.format(soma))
