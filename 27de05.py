def ex009():
    x1=float(input("Digite o numero 1 "))
    x2=float(input("Digite o numero 2 "))
    x2_ao_quadradio=x2**2
    x1_ao_quadrado=x1**2
    resultado=x1_ao_quadrado+x2_ao_quadradio
    return resultado


def comida():
    pápá=int(input("Digite quantos kilos sera fracionado    "))
    pápá_em_gm=pápá*1000
    dias=pápá_em_gm/50
    print("A comida dururá %d dias."% (dias))

comida()

    
