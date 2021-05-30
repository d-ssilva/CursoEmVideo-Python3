"""Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo
   teclado, no final mostre a matriz na tela. com a formação correta."""
l_1 = []
l_2 = []
for l in range(0, 3):
    print('=' * 30)
    print(f'Linha {l + 1}')
    l_2.clear()
    for c in range(0, 3):
        l_2.append(int(input(f'{c + 1}ª- Coluna: ')))
    l_1.append(l_2[:])
# ==| EXIBIÇÃO DE INFO |==
print('='*30)
print(f'{"LISTA COMPOSTA":^30}')
print('='*30)
for l in range(0, 3):
    print(f'{l_1[l]}')
print('='*30)
