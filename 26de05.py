def ex001():
    name=input("Digite seu nome ")
    idade=int(input("Digite sua idade "))
    grana=float(input("Digite o quanto rico vc é"))
    print("%s tem %d anos e R$%-5.2f no bolso." %(name,idade,grana))
ex001()