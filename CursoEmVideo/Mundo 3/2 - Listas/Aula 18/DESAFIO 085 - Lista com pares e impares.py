"""Crie um app onde o user possa digitar sete valores numéricos e cadastre-os em uma lista_geral única
   que mantenha separados os valores pares e impares. No final, mostre os valores pares e impares em
   ordem crescente"""
l_geral = []
l_par = []
l_impar = []
l_geral.append(l_par[:])
l_geral.append(l_impar[:])
for i in range(0, 7):
    num = int(input(f'{i+1}°- Número: '))
    if num % 2 == 0:
        l_geral[0].append(num)
    else:
        l_geral[1].append(num)
print('-='*30)
print(f'Lista de numeros pares: {sorted(l_geral[0])}')
print('-'*60)
print(f'Lista de números impares: {sorted(l_geral[1])}')
print('-='*30)
