#Desenvolver um sistema simples de cadastro de produtos utilizando apenas as operações:
#Create (Criar/Cadastrar)
#Read (Ler)
#O sistema deverá permitir:
#1 - Cadastrar produto
#2 - Listar produtos
#3 - Cadastrar preço
#4 - Listar produtos com preço
#0 - Sair

#REGRAS DO SISTEMA:
#Impedir que o sistema liste preços se não houver produtos cadastrados
#Exibir o valor total de todos os produtos cadastrados
#Mostrar o produto mais caro

def cadastrarN(nome):
    nomes.append(nome)

def lerN():
    if len(nomes) > 0:
        for i in range(len(nomes)):
            print(nomes[i])
    else:
        print("não há produtos cadastrados")
        

def cadastarP(preço):
    preços.append(preço)

def listarNP(nome,preço):
    if len(nomes) < 0:
        print("não há produtos cadastrados")
    else:
        lista = {
            'produto:': nome, 'preço:': preço
        }
        listas.append(lista)
        for i in range(len(listas)):
            print(listas[i])
        ordenada = max(preços)
        lugar = preços.index(ordenada)
        prod = nomes.pop(lugar)
        print(f"produto mais caro: {prod}: R${ordenada}0")
        nomes.insert(lugar,prod)

nomes = []
preços = []
listas = []
while True:
    print("digite 1 para cadastrar produto")
    print("digite 2 para listar produto")
    print("digite 3 cadastrar preço")
    print("digite 4 para lisatr produto com o preço")
    print("digite 0 para sair")
    opçao = int(input("digite opção desejada:"))
    match(opçao):
        case 1:
            nome = input("digite o nome do produto:")
            cadastrarN(nome)
        case 2:
            lerN()
        case 3:
            preço = float(input("digite o preço do produto:"))
            cadastarP(preço)
        case 4:
            listarNP(nome,preço)
        case 0:
            print("programa finalizado")
            break
        case _ :
            print("opção invalida")