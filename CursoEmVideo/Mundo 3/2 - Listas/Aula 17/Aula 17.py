#  LISTAS SÃO MUTÁVEIS E SE DIFERENCIÃO DAS TUPLAS PELOS COLCHETES
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
lanche.append('lazanha')  # append ADICIONA lasanha para no último índice na lista_geral
lanche[3] = 'sorvete'
print(lanche[3])
"""----------------------------------------------------------------------------------------------------------"""
lanche.insert(0, 'hot-dog')  # adciona hot-dog na posição onde estava hamburguer, o emporrando para frente -> 01
print(lanche)
"""----------------------------------------------------------------------------------------------------------"""
#  Existem três comandos para deletar um item na lista_geral:
del lanche[3]
lanche.pop(3)
if 'pizza' in lanche:
    lanche.remove('pizza')
lanche.pop()  # remove o último item da lista_geral
print(lanche)
"""----------------------------------------------------------------------------------------------------------"""
valores = list(range(4, 11))  # uma forma simplificada de criar uma lista_geral de 4 a 10
print(valores.sort(reverse=True))  # organiza em ordem DERESCENTE
"""----------------------------------------------------------------------------------------------------------"""
