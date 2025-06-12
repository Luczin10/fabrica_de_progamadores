def lê_binário():
    try:
        foto=open("junho/teste/binary.jpg", "rb")
        fotos2=foto.read()
        for linha in range(0,100):
            with open(f"junho/teste/{linha}.jpg", "wb") as fs1:
                fs1.write(fotos2)
    except FileNotFoundError as e:
            print('Arquivo não existe! -_-|||', e)
    except IOError as e:
        print('Deu algo errado @_@') 
    print("OK! ~_~")
    foto.close()
lê_binário()


