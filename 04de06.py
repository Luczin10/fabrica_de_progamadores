L=[5,9,13]
for x,e in enumerate(L):
    print("[%d]%d"%(x,e))


    def mat(x,y):
        try:
            result=x/y
        except ZeroDivisionError:
            print("Não ultilize zero seu imbecil")
        except:
            print("\033[91m Algo deu errado")
        finally:
            print("\033[92m Vamos de novo?]")
mat(13,0)