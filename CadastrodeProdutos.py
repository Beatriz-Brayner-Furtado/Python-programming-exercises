#Desenvolver um sistema de cadastro de produtos:

#O sistema deverá permitir:
#1 - Cadastrar produto
#2 - Listar produtos
#3 - Cadastrar preço
#4 - Listar produtos com preço
#5 - Atulizar produto ou preço
#6 - excluir
#7 - pesquisar
#0 - Sair

#REGRAS DO SISTEMA:
#Impedir que o sistema liste preços se não houver produtos cadastrados
#Exibir o valor total de todos os produtos cadastrados
#Mostrar o produto mais caro
#Fazer UDP

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
        for i in range(len(nomes)):
            print(f"{i+1}: {nomes[i]}: R${preços[i]}0")
        ordenada = max(preços)
        lugar = preços.index(ordenada)
        prod = nomes.pop(lugar)
        print(f"produto mais caro: {prod}: R${ordenada}0")
        nomes.insert(lugar,prod)

def atualizar():
    while True:
        opc = input("deseja atualizar o produto ou o preço? (produto/preço):").lower()
        if opc == "produto":
            for i in range(len(nomes)):
                print(f"{i+1}: {nomes[i]}")
            atua_pro = int(input("digite indice de quem deseja atualizar:"))
            if 1<= atua_pro and atua_pro <= len(nomes):
                i = atua_pro - 1
                novo_nome = input("digite novo produto:")
                nomes[i] = novo_nome
                break
            else:
                print("opção nao consta na lista")
            break
        if opc == "preço":
            for i in range(len(preços)):
                print(f"{i+1}: {preços[i]}")
            atua_pre = int(input("digite indice de quem deseja atualizar:"))
            if 1<= atua_pre and atua_pre <= len(preços):
                i = atua_pre - 1
                novo_preço = float(input("digite novo preço:"))
                preços[i] = novo_preço
                break
            else:
                print("opção nao consta na lista")
        break

def excluir():
    for i in range(len(nomes)):
        print(f"{i+1}: {nomes[i]}")
    exc = int(input("digite o indice de quem deseja excluir:"))
    if 1<= exc and exc <= len(nomes):
        i = exc - 1
        nomes.pop(i)
        preços.pop(i)

def pesquisar():
    pesquisa = input("nome do produto que deseja encontrar:")
    for i in range(len(nomes)):
        if nomes[i] == pesquisa:
            print(f"{i+1}: {nomes[i]}")
        else:
            print("produto não consta na lista")

nomes = []
preços = []
listas = []
while True:
    print("digite 1 para cadastrar produto")
    print("digite 2 para listar produto")
    print("digite 3 cadastrar preço")
    print("digite 4 para lisatr produto com o preço")
    print("digite 5 para atulizar produto ou preço")
    print("digite 6 para excluir")
    print("digite 7 para pesquisar")
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
        case 5:
            atualizar()
        case 6:
            excluir()
        case 7:
            pesquisar()
        case 0:
            print("programa finalizado")
            break
        case _ :
            print("opção invalida")