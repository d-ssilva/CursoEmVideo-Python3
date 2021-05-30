"""Sabendo que uma váriavel uma vez trabalhada numa função, a mesma se torna LOCAL, diferente das que são
   declaradas no decorrer do processo principal do app, as variáveis GLOBAIS.
   - Para que uma determinada variável tenha efeito global uma vez que passou por uma função, deve-se atribuir o
     comando 'global' precedido da variável, logo abaixo da linha def ou docstrg."""

def teste(b):
    global a  # PERMITINDO QUE A VARIÁVEL TENHA EFEITO GLOBAL APÓS O PROGRAMA
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


  # PROGRAMA PRINCIPAL - Campo Geral
a = 5
teste(a)
print(f'A fora vale {a}')
