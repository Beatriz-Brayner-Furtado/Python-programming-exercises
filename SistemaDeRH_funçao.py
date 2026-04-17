#O programa deve ser capaz de manipular :

#nome do funcionário
#salario 
#bonus (mediante quantidade de horas extras trabalhadas a ser adicionado no valor final do salário) calculado da seguinte forma: bonus = horas_extras * 50
#O sistema deve exibir ao final:
#Nome do funcionário
#Salário base
#Valor do bônus
#Salário final
#Valor do desconto (se houver)

#Regras REAIS de empresa:
#Cada hora extra vale R$ 50,00
#Se o salário for maior que R$ 10.000,00, aplicar desconto de 10% sobre o salário com bônus.
#Se o salário for menor que R$5.000,00, aplicar adicional de 5% sobre o salário com bônus.
#Se o salário estiver entre R$5.000,00 e R$ 10.000,00, não aplicar desconto nem adicional.

def menor(vabonus,salariob):
    vbonus = bonus * 1.5
    salariof = vbonus + salariob
    salariofs.append(salariof)
    vabonus.append(vbonus)

def maior(vbonus,salariob,bonus):
    vbonus = bonus * 0.9
    salariof = vbonus + salariob
    salariofs.append(salariof)
    vabonus.append(vbonus)
    desconto = bonus * 0.1
    vdescontos.append(desconto)

def meio(bonus,salariob):
    vbonus = bonus
    salariof = vbonus + salariob
    salariofs.append(salariof)
    vabonus.append(vbonus)

def listar():
    for i in range(qtde):
        print(f"{i+1}:nome:{nomes[i]}")
        print(f"{i+1}:sálario base:{salariobs[i]}")
        print(f"{i+1}:valor do bonus:{vabonus[i]}")
        print(f"{i+1}:sálario final:{salariofs[i]}")
        if salariobs [i] > 10000:
            print(f"{i+1}:valor do desconto:{vdescontos[i]}")
        else:
            continue


nomes = []
salariobs = []
vabonus = []
salariofs =[]
vdescontos = []

qtde = int(input("quantos folhas de pagamento gostaria de realizar:"))
for i in range(qtde):
    nome = input("nome do funcionário:")
    salariob = float(input("salário base do funcionário:"))
    horaextras = float(input("horas extras trabalhadas pelo funcionário:"))
    bonus =  horaextras * 50
    nomes.append(nome)
    salariobs.append(salariob)
    if salariobs [i] < 5000:
        menor(vabonus,salariob)
    elif salariobs [i] > 10000:
        maior(salariob,bonus)
    else:
        meio(bonus,salariob)
        
listar()