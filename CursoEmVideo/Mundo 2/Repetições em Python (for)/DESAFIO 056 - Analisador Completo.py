"""Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 PESSOAS, no final do programa, mostre:
- A MÉDIA de IDADE do grupo;
- Qual é o nome do HOMEM mais VELHO;
- Quantas MULHERES tem menos de 20 ANOS;"""
contm = 0  # contador de mulheres jovens
ivelho = 0  # varável idade para separar o homem mais velho
totanos = 0  # váriável para média de idade


def limpa():
  print('\n'*10)
for c in range(1, 5):
    nome = input('Digite o nome da {}º cadastro: '.format(c))  # inserção do nome
    idade = int(input('Digite quantos anos tem {}: '.format(nome.upper())))  # inserção de idade
    totanos += idade  # Acumulador de idade para média
    sexo = str(input('Informe o sexo de {}.\n- [M/ F] Digite aqui: '.format(nome))).upper()
    if c == 1 and sexo in 'Mm':
        ivelho = idade
        nvelho = nome
    if sexo in 'Mm' and idade > ivelho:  # Decidindo o homem mais velho cadastrado
        ivelho = idade
        nvelho = nome

    if (sexo == 'F') and (idade < 20):
        contm += 1  # Contador de idade para mulheres < dos 20 anos

    else:
        print('Sexo ou idade inserida inválidos!')
    limpa()

print('- A média de idade é {}'.format(totanos / 4))
print('- {} é o mais velho.'.format(nvelho))
print('- {} mulheres mais abaixo de 20 anos'.format(contm))