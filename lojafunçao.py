#O programa deve:

#Mostrar um menu com opções:

#1 - Cadastrar cliente
#2 - Cadastrar produto
#3 - Realizar venda
#0 - Sair

#Permitir cadastrar um cliente informando nome e idade
#Permitir cadastrar um produto informando nome e preço
#Permitir realizar uma venda informando:

#Nome do produto
#Preço unitário
#Quantidade comprada

#Calcular o valor total da compra
#Exibir o valor final da compra na tela

#Regras do sistema:
#O cliente pode ser cadastrado como maior ou menor de idade
#O preço do produto deve ser maior que zero
#O valor total da venda deve ser calculado multiplicando preço × quantidade
#Se (if) o valor total da compra for maior ou igual a 500 reais, aplicar 10% de desconto
#Senão (else), manter o valor normal
#O sistema deve funcionar em loop usando while True até o usuário escolher sair

nomeclis = []
idades = []
nomepros = []
preopros = []
nomevendas = []
preçounis = []
vts = []
vtdiscontos = []
def cadastrarC():
    nomecli = input("digite o nome do cliente:")
    idade = int(input("digite a idade do cliente:"))
    if idade >= 18:
        print("cliente maior de idade")
    else:
        print("cliente menor de idade")
    nomeclis.append(nomecli)
    idades.append(idade)

def cadastrarP():
    nomepro = input("digite o nome do produto:")
    while True:
        preçopro = float(input("digite o preço do produto:"))
        if preçopro <= 0:
            print("preço do produto deve ser maior que 0")
        else:
            break
    nomepros.append(nomepro)
    preopros.append(preçopro)

def realizarV():
    nomevenda = input("digite o nome do produto:")
    while True:
        preçouni = float(input("digite o preço unitário do produto:"))
        if preçouni <= 0:
            print("preço unitário deve ser maior que 0")
        else:
            break
    qtde = int(input("digite a quantidade comprada:"))
    vt = preçouni * qtde
    if vt >= 500:
        vtdesconto = vt*0.9
        print(f"valor final da compra: R${vtdesconto}")
        vtdiscontos.append(vtdesconto)
    else:
        print(f"valor final da compra: R${vt}")
        vts.append(vt)
    nomevendas.append(nomevenda)
    preçounis.append(preçouni)


def invalidar():
    print("opção invalida")

while True:
    print("digite 1 para cadastrar cliente")
    print("digite 2 para cadastrar produto")
    print("digite 3 para realixar venda")
    print("digite 0 para sair")
    resp = int(input("digite a opção selecionada:"))
    match resp:
        case 1:
            cadastrarC()
        case 2:
            cadastrarP()
        case 3:
            realizarV()
        case 0:
            print("você finalizou o programa")
            break
        case _:
            invalidar()