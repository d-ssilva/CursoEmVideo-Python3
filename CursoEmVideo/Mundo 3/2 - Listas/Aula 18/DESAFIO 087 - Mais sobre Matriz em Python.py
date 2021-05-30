"""Aprimore o desafio anterior, mostrando no final:
   A) A soma de todos os valores pares digitados; R: var incremental
   B) A soma dos valores na terceira coluna;
   C) O maior valor da segunda linha; R: max."""
l_1 = []
l_2 = []
tot_par = 0
num = 0
s_coluna = 0
for l in range(0, 3):
    print('=' * 30)
    print(f'Linha {l + 1}')
    l_2.clear()
    for c in range(0, 3):
        num = int(input(f'{c + 1}°- Coluna: '))
        l_2.append(num)
        if num % 2 == 0:
            tot_par += num
        if (l == 0) and (c == 2) or (l == 1) and (c == 2) or (l == 2) and (c == 2):
            s_coluna += num
    l_1.append(l_2[:])
# ==| EXIBIÇÃO DE INFO |==
print('='*30)
print(f'{"LISTA COMPOSTA":^30}')
print('='*30)
for l in range(0, 3):
    print(f'{l_1[l]}')
print('='*30)
print(f'Soma total de todos os valores pares é: {tot_par}')
print('='*30)
print(f'O maior valor da 2ª linha é: {max(l_1[1])}')
print('='*30)
print(f'A soma dos valores da 3ª coluna é: {s_coluna}')
print('='*30)
