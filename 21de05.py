def tabuada():

    n=int(input("Tabuada de: "))
    x=1
    while x<=10:
        print(n*x)
        x=x+1


def ex006():
    x1=int(input("Tabuada de: "))
    x2=1
    while x2<=10:
        conta=(f"{x1}*{x2}")
        resultado=x1*x2
        print(f"conta= {conta}   resultado= {resultado}")




def ex007():
    num1=int(input("tabuada de : "))
    x2=int(input("qual o inicio da tabuada?"))
    tabuada=int(input("Ate qual numero a tabuada vai?"))
    while x2<=tabuada:
        conta=(f"{num1}*{x2}")
        resultado=num1*x2
        print(f"conta= {conta}   resultado= {resultado}")
        x2=x2+1
        continue

def ex008():
    s=0
    while True:
            v=int(input("Digite um numero a somar ou 0 para sair"))
            if v==0:
                 break
            
            s=s+v
    print(s)

def ex009():
    L=[]
    while True:
        n=int(input("Digite numeros para calcular a media. Ou digite 0 para sair   "))
        if n==0:
            break
        L.append(n)
        resultado=L+L/len(L)
        print(resultado)
ex009()
   






