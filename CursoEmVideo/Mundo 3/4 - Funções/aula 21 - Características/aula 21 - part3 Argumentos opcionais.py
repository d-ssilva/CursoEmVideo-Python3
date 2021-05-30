  # ARGUMENTOS OPCIONAIS
  # parametros que são seguidos de = 0 na linha def, são opcionais, ou seja, caso o user não informe a o paremetro
  # terá valor 0 como foi defindo pela função
def somar(a = 0, b = 0, c = 0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return:
    Função criada por Gustavo Guanabara do canal CursoemVideo
    """
    s = a + b + c
    print(f'A soma vale {s}')