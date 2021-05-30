"""Crie um programa onde o user possa digitar 5 valores numéricos e cadastre-os em uma lista_geral.
   já na posição correta de inserção (sem usar o sort()).

   No final, mostre a lista_geral ordenada na tela."""
lista = []
for c in range(0, 5):
    print('-' * 30)
    num = int(input(f'Digite o {c+1}° valor: '))
    if c == 0 or num > lista[-1]: # Se ele é primeir ou maior que o último
        lista.append(num)
        print('Adicionei no \033[2:33mFINAL\033[m da lista_geral')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)  # Faz uma varredura na lista_geral afim de verificar se os valores inseridos são
                                        # maiores que o user digitou
                print(f'Adicionei na posição \033[33m{pos}\033[m da lista_geral')
                break
            pos += 1
print('='*30)
print(f'Os valores digitados em ordem foram {lista}')
