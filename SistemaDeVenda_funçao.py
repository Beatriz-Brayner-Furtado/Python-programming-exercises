#Criar um sistema capaz de registrar vendas e gerar informações financeiras básicas.

#O programa deve ser capaz de manipular :
#nome do produto
#preco unitario
#quantidade do estoque
#valor_total da compra

#Regras comerciais:
#Não permitir preço menor ou igual a zero
#Não permitir quantidade negativa
#Se uma venda ultrapassar , sinalizar como: "VENDA IMPORTANTE"

def classificar():
    for i in range(qtde):
        print(f"{i+1}:valor total da compra:{vts[i]}")
        if vts [i] > metas [i]:
            print("VENDA IMPORTANTE")
        else: 
            continue
def calcular(preço,estoque):
    vt = preço * estoque
    vts.append(vt)

nomes = []
preços = []
estoques = []
metas = []
vts = []
qtde = int(input("digite o número de vendas que deseja fazer:"))
for i in range(qtde):
    nome = input("digite nome do produto:")
    meta = float(input("digite meta da empresa:"))
    while True:
        preço = float(input("digite preço unitário:"))
        if preço <= 0:
            print("o preço unitário deve ser maior que zero:")
        else:
            preços.append(preço)
            break
    while True:
        estoque = int(input("digite a quantidade do estoque disponivel:"))
        if estoque < 0:
            print("a quantidade no estoque não pode ser negativa")
        else:
            estoques.append(estoque)
            break
    calcular(preço,estoque)
    nomes.append(nome)
    metas.append(meta)
classificar()