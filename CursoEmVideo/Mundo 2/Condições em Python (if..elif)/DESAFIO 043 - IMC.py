"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida """

peso = float(input('Insira seu peso (Kg): '))
alt = float(input('Insira sua altura (metros): '))
imc = peso / (alt ** 2)
print ('O IMC é de: {:.1f}'.format(imc))
print('Você esta em ', end='')
if imc < 18.5:
    print('ABAIXO DO PESO NOMRAL')
elif 18.5 <= imc < 25:
    print('PESO NORMAL')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc <= 40:
    print('OBESIDADE')
elif imc >= 40:
    print('OBESIDADE MÓRBIDA')
