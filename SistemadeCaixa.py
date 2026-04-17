#Você foi contratado para criar um programa de caixa para uma loja esportiva multimarcas de tênis. 
#O sistema deve permitir que o atendente registre compras de tênis, calcule o total e processe o pagamento.

# Regras do sistema
#O programa deve rodar em while True para permitir adicionar vários itens à compra.
#Use match case para tratar as opções escolhidas.
#Sempre que o usuário escolher um item (1 a 4):
#Perguntar quantas unidades o cliente deseja
#Calcular o valor do item 
#Adicionar ao total da compra
#Registrar o item e a quantidade em listas

#Quandoo usuário escolher 5 (Finalizar compra):
#Mostraro resumo da compra com todos os itens e quantidades
#Mostrar o total a pagar
#Chamara função de pagamento

#Formas de pagamento
#Após mostrar o total, o sistema deve perguntar a forma de pagamento:
#1 - Dinheiro
#2 - Cartão
#3 - PIX

#Use match case novamente.

#Dinheiro:
#Perguntar valor pago
#Calcular e mostrar troco se houver
#Se o valor pago for menor que o total, avisar que é insuficiente e pedir novamente

#Cartão:
#Perguntar se deseja parcelar
#Se sim → perguntar o número de parcelas e mostrar aprovação
#Se não → mostrar aprovação do pagamento

#PIX:
#Mostrar apenas: "Pagamento via PIX aprovado."

#Restrições
#Usar listas para produtos, preços, itens do pedido e quantidades
#Usar funções para organizar o código
#Usar while True e match case
#Não usar estruturas complexas como dicionários ou classes

def registrar(qtde,valor):
    qtdes.append(qtde)
    valores.append(valor)

def adicionar(qtde, valor):
    total = qtde * valor
    totals.append(total)  

def listar():
    for i in range(len(valores)):
        print(f"valor do item {i+1}: R${valores[i]}0, quantidade do item {i+1}: {qtdes[i]}")
    print(f"valor total a pagar: R${pagar}0")
    
def pagamento(pagar):
    while True:
        print("digite 1 para dinheiro")
        print("digite 2 para cartão")
        print("digite 3 para pix")
        forma = int(input("digite forma de pagamento escolhida:"))
        match(forma):
            case 1:
                valor_pago = float(input("digite o valor pago pelo cliente:"))
                troco = valor_pago - pagar
                if troco > 0:
                    print(f"troco de R${troco}0")
                    break
                elif troco < 0:
                    print("quantia insuficiente, tentar novamente")
                else:
                    print("pagamento realizado com sucesso")
                    break
            case 2:
                parcelar = input("deseja parcelar ? (s/n):").lower()
                if parcelar == "s" or parcelar == "sim":
                    parcela = int(input("digite o número de parcelas:"))
                    print("pagamento aprovado")
                    break
                elif parcelar == "n" or parcelar == "nao" or parcelar == "não":
                    print("pagamento aprovado")
                    break
                else:
                    print("opção invalida, tentar novamente")
            case 3:
                print("pagamento via PIX aprovado")
                break

qtdes = []
valores = []
totals = []
while True:
    print("digite 1 a 4 para cadastrar compra")
    print("digite 5 para finalizar compra")
    opc = int(input("digite a opção desejada:"))
    match(opc):
        case 1:
            qtde = int(input("digite a quantidade de unidades desejadas:"))
            valor = float(input("valor do item:"))
            registrar(qtde,valor)
            adicionar(qtde, valor)
            pagar = sum(totals)
        case 2:
            qtde = int(input("digite numero de unidades desejadas:"))
            valor = float(input("valor do item:"))
            registrar(qtde,valor)
            adicionar(qtde, valor)
            pagar = sum(totals)
        case 3:
            qtde = int(input("digite numero de unidades desejadas:"))
            valor = float(input("valor do item:"))
            registrar(qtde,valor)
            adicionar(qtde, valor)
            pagar = sum(totals)
        case 4:
            qtde = int(input("digite numero de unidades desejadas:"))
            valor = float(input("valor do item:"))
            registrar(qtde,valor)
            adicionar(qtde, valor)
            pagar = sum(totals)
        case 5:
            listar()
            pagamento(pagar)
            break