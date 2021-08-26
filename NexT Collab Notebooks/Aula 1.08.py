#Faça um Programa que pergunte quanto você ganha por hora
#e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

sal = float (input('Informe o quanto você ganha por hora: '))
horas = int (input('Informe quantas horas foram trabalhadas no mês: '))

print(f'O seu salário do mês será de R${sal*horas:.2f}.')
