numero = soma = 0
while True:  # "True" faz com que o laço repita tudo pra sempre, até que o comando "break" seja identificado
    numero = int(input('Digite um número: '))
    if numero == 999:
        break  # o laço para quano a variável extenso for igual a 999
    soma += numero
print(f'A soma vale {soma}')
