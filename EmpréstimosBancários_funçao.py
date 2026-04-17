#Um banco registrou pedidos de empréstimo de vários clientes. 
#As informações foram armazenadas em listas separadas, onde cada índice corresponde ao mesmo cliente. 

#nomes = ["Carlos", "Ana", "Juliana", "Roberto", "Patricia"] 
#idades = [22, 45, 37, 29, 61]
#salarios = [2500.00, 8000.00, 12000.00, 4000.00, 15000.00] 
#valores_emprestimo = [10000.00, 20000.00, 50000.00, 15000.00, 30000.00] 

#O programa deve: 
#Percorrer as listas usando índice. 
#Calcular a taxa de risco de cada cliente: 
#Se o empréstimo for maior que 5x o salário → "ALTO RISCO" 
#Se for entre 3x e 5x o salário → "MÉDIO RISCO" 
#Se for até 3x o salário → "BAIXO RISCO" 
#Aplicar regras adicionais: 
#Se idade for menor que 25 → aumentar o risco em um nível. 
#Se salário for maior que R$ 10.000 → reduzir o risco em um nível. 

#Mostrar para cada cliente:
#Nome
#Salário
#Valor solicitado 
#Classificação final de risco

risco = 0
def calcular(emprestimos,salarios,idades):
    for i in range(qtde):
        if emprestimos[i] > 5 * salarios[i]:
            risco = 3
        elif emprestimos[i] > 3 * emprestimos[i] and emprestimos[i] <= 5 * emprestimos[i]:
            risco = 2
        elif emprestimos[i] <= 3 * emprestimos[i]:
            risco = 1
        else:
            continue
        if idades [i] < 25:
            risco = risco +1
        else:
            continue
        if salarios [i] > 10000:
            risco = risco - 1
        else:
            continue 

def printar():
    for i in range(qtde):
        if risco <= 1:
            riscos.append("baixo risco")
        elif risco == 2:
            riscos.append("médio risco")
        elif risco >= 3:
            riscos.append("alto risco")
        else:
            continue
        print(f"{i+1}: nome do cliente: {nomes[i]}")
        print(f"{i+1}: salário do cliente: {salarios[i]}")
        print(f"{i+1}: valor solicitado: {emprestimos[i]}")
        print(f"{i+1}: classificação final de risco: {riscos[i]}")

nomes = []
idades = []
salarios = []
emprestimos = []
riscos = []
qtde = int(input("digite a quantidade de clientes que gostaria cadastrar:"))
for i in range(qtde):
    nome = input("digite nome do cliente:")
    idade = int(input("digite a idade do cliente:"))
    salario = float(input("digite o salário do cliente:"))
    emprestimo = float(input("digite valor do empréstimo solicitado:"))
    nomes.append(nome) 
    idades.append(idade)
    salarios.append(salario)
    emprestimos.append(emprestimo)
    calcular(emprestimos,salarios,idades)
printar()