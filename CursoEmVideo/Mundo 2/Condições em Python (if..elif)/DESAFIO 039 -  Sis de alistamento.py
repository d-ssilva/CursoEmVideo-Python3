"""     Faça um programa que:
 - leia o ano de nascimento de um jovem                         (V)
        e informe,de acordo com a sua idade
 - se ele ainda vai se alistar ao serviço militar,              (V)
 - se é a hora exata de se alistar ou,                          ()
 - se já passou do tempo  do alistamento.                       (V)
        Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""
from datetime import datetime
from time import sleep

def slep():
    sleep(0.2)
# inserindo informações
slep()
print("|", "="*10, 'BEM VINDO AO SISTEMA DE ALISTAMENTO DO BRASIL!', "="*10, "|")
print(' - A idade MINIMA para o serviço militar obrigatório é de 17 anos.')
slep()
ano_nasc = int(input('Digite os QUATRO digitos do seu ano de nascimento: '))
slep()
print('Por favor, aguarde...')
sleep(2)

# variável usada para processar a idade do usuário
ano_atual = datetime.now()
ano_atual = ano_atual.year
idade_user = ano_atual - ano_nasc
print('Você tem {} anos.'.format(idade_user))

# estrutura condicional aninhada
if idade_user == 17:
    print('Você esta na idade certa para o alistamento!')
elif idade_user > 17:
    x = idade_user - 17
    y = ano_atual - x
    print('Você atrasou {} anos para o alistamento, você deveria ter se alistado em {}.'.format(x,y))
elif idade_user < 17:
    x = ano_nasc + 17
    print('Você não tem a idade minima para o alistamento, você deverá voltar em {}.'.format(x))
else:
    print('Erro de processamento')
print('Fim de programa!')