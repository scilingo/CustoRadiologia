import csv
import pyfiglet
import math
from collections import defaultdict

text = pyfiglet.figlet_format("Custo Radiologia")

def totalReceita():
  filename = open('Radiologia.csv', 'r')
  file = csv.DictReader(filename)
  receita = []
  for col in file:
    receita.append(col['VALOR DO PROCEDIMENTO'])
  receita = [w.replace(',', '.') for w in receita]
  floatzin = [float(x) for x in receita]
  soma = sum(floatzin)
  print("\nO valor total da receita é de R$%s." % round(soma))


def receitaServico():
  filename = open('Radiologia.csv', 'r')
  file = csv.DictReader(filename)
  servico = []
  valor = []
  final2 = []
  final = []
  for col in file:
    servico.append(col['SERVICO'])
    valor.append(col['VALOR DO PROCEDIMENTO'])
  valor = [w.replace(',', '.') for w in valor]
  floatzin = [float(x) for x in valor]
  soma = sum(floatzin)
  list_of_tuples = list(zip(servico, valor))
  d = defaultdict(float)
  for x, y in list_of_tuples:
    d[x] += float(y)
  calculo = [(x, round(y, 2)) for x, y in d.items()]
  print("\nTotal de receitas baseadas pelos serviços:")
  print("SERVIÇOS          VALOR")
  for x in calculo:
    print(x[0], " | ", "R$%s" % x[1])


def qntServicoTotal():
  filename = open('Radiologia.csv', 'r')
  file = csv.DictReader(filename)
  servico = []
  qntdServ = []
  for col in file:
    servico.append(col['SERVICO'])
    qntdServ.append(col['QUANTIDADE DO SERVICO'])
  list_of_tuples = list(zip(servico, qntdServ))
  d = defaultdict(int)
  for x, y in list_of_tuples:
    d[x] += int(y)
  calculo = [(x, round(y, 2)) for x, y in d.items()]
  print("\nQuantidade de serviços prestados por serviços e total:")
  print("SERVIÇOS         QNTD SERVIÇOS")
  for x in calculo:
    somar = sum(tup[1] for tup in calculo)
    print(x[0], " | ", x[1])
  print("\nTotal de %s serviços." % somar)


def qntPacientesAtend():
  filename = open('Radiologia.csv', 'r')
  file = csv.DictReader(filename)
  paciente = []
  result = []
  for col in file:
    paciente.append(col['PACIENTE'])
  for i in paciente:
    if i not in result:
      result.append(i)
  print("\nO total de pacientes atendidos foi de %s." % len(result))


if __name__ == "__main__":
  print(text)
  print("Por favor, selecione a função desejada. \n 1- O total de receita \n 2- O total de receita por serviço \n 3- Quantidade de serviço prestado por serviço e total \n 4- Quantidade de pacientes atendidos")
  escolha = int(input("Digite uma das funções: "))

  if escolha == 1:
    totalReceita()
  elif escolha == 2:
    receitaServico()
  elif escolha == 3:
    qntServicoTotal()
  elif escolha == 4:
    qntPacientesAtend()
