"""RETURN - permite que uma determinada função ao ser chamada, consiga substituir o uso do 'print' jogando o
   resultado de um processo numa variável ou print global, apenas para retornar rsrs"""


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Os resultador foram {r1, r2, r3}')

# OU

print(f'Os resultados foram {somar(3, 2, 5), somar(2, 2), somar(6)}')
