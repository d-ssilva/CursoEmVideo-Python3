  # DOCSTRINGS
  # permite que o user crie uma documentação a respeito de um comando criado pelo mesmo. Basta digitar 3 aspas duplas,
  # logo abaixo da linha def
def contador(i,f,p):
    """
    Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara do canal CursoemVideo
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')