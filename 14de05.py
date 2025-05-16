def banco():
    conta_corrente=float(input("Digite seu saldo bancario "))
    Deposito=float(input("Digite seu deposito  "))
    if conta_corrente>=Deposito:
        data=int(input("Digite quantos meses sera feito sua poupança "))
        Rendimento=Deposito*(1.3/100)*data
        saldo=Rendimento+conta_corrente
        print(f"Seu rendimento é de {Rendimento} e seu saldo atual é de {saldo}")
    else:
        print("Você não tem este dinheiro ")
def jornal():

    tempC=float(input("Digite sua temperatura"))
    tempF=(9*tempC+160)/5
    print(f"Sua temperatura em F é {tempF}")


def mat():
    num1=float(input("Digite o numero 1 "))
    num2=float(input("Digite o numero 2 "))
    if num1>num2:
        print("numero 1 é maior que numero2")
        print("esta é a diferença ", num1-num2)
    else:
        print("O numero 2 é maior que numero 1")
        print("esta é a diferença", num2-num1)

def finaça():
    num1=float(input("Digite o numero 1 "))
    num2=float(input("Digite o numero 2 "))
    num3=''
    if num2>num1:
        num3=""
        num3=num1
        num1=""
        num1=num2
        num2=num3
        print("o numero 1 é maior e a diferença é de ",num1-num2)
    else:
        print("o numero 1 é maior e a diferença é de ",num1-num2)
finaça()