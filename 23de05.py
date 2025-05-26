#def para():
    #lista=[20,11,34,17638,9.836,5436,637,12,245,234,855,37,358,4272,783936239,345,926,8252830,32,8,634,6,98,1]
   # minimo=lista[0]
   # for e in lista:
        #if e < minimo:
            #minimo= e
        #print(minimo)



def ex005():
    nomecliente = input("Digite seu nome para prosseguir: ")
    numerodchamada=int(input("Digite seu nuemro para chamada  "))
    sabor1="Toscana"
    sabor2="muçarela"
    sabor3="marguerita"
    sabor4="calabresa"
    preço1=50.99
    preço2=49.50
    preço3=50.50
    preço4=57.99
    quantidade=int(input("Digite quantas pizzas ira querer"))
    pedido=int(input(f"Digite qual pizza você ira querer     1-{sabor1},{preço1}     2-{sabor2},{preço2}      3-{sabor3},{preço3}      4-{sabor4},{preço4}"))
    if pedido==1:
        custo=quantidade*preço1
        print(custo)
        



for t in range(3,33,3):
    print(t, end=" ")
    

