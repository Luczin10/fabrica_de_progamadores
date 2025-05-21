
import math
def bhaskara():

    A=float(input())
    B=float(input())
    C=float(input())
    delta=B**2-4*A*C
    

    if delta>=0:
        x1=(-B+ math.sqrt(delta))/2*A
        x2=(-B- math.sqrt(delta))/2*A
        print(x1,x2)
    else:
        print("erro")


def exercicio1 ():
    num1=float(input("Digite o numero 1 "))
    num2=float(input("Digite o numero 2 "))
    if num1>num2:
        print("numero 1 é maior que numero2")
        print("esta é a diferença ", num1-num2)
    else:
        print("O numero 2 é maior que numero 1")
        print("esta é a diferença", num2-num1)



def exercicio2():
    R=int(input("Digite o raio"))
    pi=3.14
    A=pi*R**2

    print(A)

def idade():
    nascimento=int(input("Digite seu ano de nascimento "))
    ano_atual=2025
    idade_atual=ano_atual-nascimento+17
    print(idade_atual)


def hipotenusa():
    ang1=float(input("digite o angulo 1 "))
    ang2=float(input("Digite o angulo 2 "))
    ang3= ang1**2 + ang2**2
    resultado=float( math.sqrt(ang3))
    print(resultado)
hipotenusa()