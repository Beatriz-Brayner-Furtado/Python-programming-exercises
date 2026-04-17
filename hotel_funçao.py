#O programa deve:

#Mostrar um menu com opções:
#1 - Cadastrar hóspede
#2 - Cadastrar quarto
#3 - Fazer reserva
#0 - Sair

#Permitir cadastrar um hóspede informando nome e documento
#Permitir cadastrar um quarto escolhendo o tipo: simples ou luxo

#Permitir realizar uma reserva informando:
#Nome do hóspede
#Tipo do quarto
#Quantidade de dias da estadia

#Calcular o valor total da reserva
#Exibir o valor final da hospedagem

#Regras do sistema:
#O documento do hóspede deve ter pelo menos 5 caracteres
#O quarto simples custa 150 reais por dia
#O quarto luxo custa 300 reais por dia
#O valor total da reserva deve ser calculado multiplicando diária × quantidade de dias
#Se (if) a quantidade de dias for maior ou igual a 7, aplicar 15% de desconto
#Senão (else), cobrar o valor normal
#O sistema deve funcionar em loop usando while True até o usuário escolher sair

nomeHs = []
documentos = []
quartoRs = []
dias = []
quartos = []
vts = []
vtdiscontos = []
nomeRs = []

def cadastrarH():
    nomeH = input("digite nome do hóspede:")
    while True:
        documento = input("digite documento do hóspede:")
        tamanho = int(len(documento))
        if tamanho < 5:
            print("documento do hóspede deve ter pelo menos 5 caracteres")
        else:
            break
    nomeHs.append(nomeH)
    documentos.append(documento)
def cadastrarQ():
    while True:
        quarto = input("gostaria de qual quarto (simples/luxuoso), simples: R$150 por dia e luxuoso R$300 por dia:").lower()
        if quarto == "luxuoso" or quarto == "simples":
            break
        else:
            print("comando inválido, tentar novamente")   
    quartos.append(quarto)

def reserva():
    nomeR = input("digite o nome do hóspededa reserva:")
    while True:
        quartoR = input("gostaria de qual quarto (simples/luxuoso):").lower()
        if quartoR == "simples":
            quartoR = 150
            break
        elif quartoR == "luxuoso":
            quartoR = 300
            break
        else:
            print("comando inválido, tentar novamente")
    dia = int(input("digite a quantidade de dias da estadia:"))
    vt = quartoR * dia
    if dia >= 7:
        vtdisconto = vt * 0.85
        print(f"valor total = R${vtdisconto}")
        vtdiscontos.append(vtdisconto)
    else:
        print(f"valor total = R${vt}")
        vts.append(vt)
    quartoRs.append(quartoR)
    nomeRs.append(nomeR)

while True:
    print("digite 1 para cadastrar hóspede")
    print("digite 2 para cadastrar quarto")
    print("digite 3 para fazer reserva")
    print("digite 0 para sair")
    resp = int(input("digite opção selecionada:"))
    match resp:
        case 1:
            cadastrarH()
        case 2:
            cadastrarQ()
        case 3:
            reserva()
        case 0:    
            print("você finalizou o programa") 
            break