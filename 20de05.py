def ex001():
    x=1
    while x<=100:
        print(x)
        x=x+1


def ex002():
    x=50
    while x<=100:
        print(x)
        x=x+1

    
def ex003():
    x=10
    while x>0:
        print(x)
        x=x-1
    print("Fogo!!!!")


def ex004():
    num1=int(input("Digite o ultimo numero a imprimir:"))
    x=0
    while x <= num1:
        if x%2 ==0:
            print(x)
        x= x+1

def ex005():
    inicio=int(input("Digite o numero 1"))
    x=0
    while x<=inicio:
        if x%2==1:
            print(x)
        x=x+1
ex005()