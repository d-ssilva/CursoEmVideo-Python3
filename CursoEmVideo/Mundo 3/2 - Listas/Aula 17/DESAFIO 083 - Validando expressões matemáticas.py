"""Crie um program onde o usuário digite a expressão qualquer que user parênteses. Seu app deverá analisar
   se a expressão passada está com os parênteses abertos e fechados na ordem correta."""
expr = input('Digite a expressão: ')
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta válida!')
else:
    print('Sua expressão esta inválida!')
