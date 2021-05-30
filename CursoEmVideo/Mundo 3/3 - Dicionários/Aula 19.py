filme = {
    'Titulo': 'Star Wars',
    'Ano': '1997',
    'Diretor': 'George Lucas'
}
print(filme.values())  # retorna todos os VALORES/DADOS do dicionário
print(filme.keys())    # retorna todos os ÍNDICES/IDENTIFICADORES
print(filme.items())   # retorna todos os Anteriores
"""================================================================================================
                        MÉTODO p/ printar um dicinário organizadamente
================================================================================================"""
for k, v in filme.items():  # K - keys; V - values
    print(f'{k} é {v}')
"""================================================================================================
                                        PARTE PRÁTICA
================================================================================================"""
pessoas = {
    'nome': 'Danilo', 'sexo': 'M', 'idade': 26
}
print(f'O {pessoas["nome"]}, tem {pessoas["idade"]} anos')
