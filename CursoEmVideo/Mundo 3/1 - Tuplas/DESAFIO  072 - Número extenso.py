"""Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
          'quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitoou o número {extenso[num]}')
    resp = input('Deseja continuar? [S/N] -> ').upper().strip()[0]
    if resp in 'N':
        break
print('Programa finalizado!')
