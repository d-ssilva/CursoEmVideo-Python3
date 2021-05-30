from time import sleep
sleep(0.5)
print('Bem-vindo ao sistema de empréstimo!')
sleep(0.5)
# inserção de valores
valorcasa = float(input('Insira o valor da casa R$'))
sal = float(input('Insira o salário: R$'))
parc = int(input('Quantos anos de financiamento? : '))
parc = parc * 12
# processamento
vparcelas = valorcasa/parc
paguser = sal * 0.3
sleep(1.2)
# estrutura condicional composta
if vparcelas <= paguser:
    print('Parabéns, empréstimo concedido!\n{}x de {:.2f}.'.format(parc, vparcelas))
else:
    print('Empréstimo negado!\n')
print('Fim de operação!')
