
with open("junho/modelo.txt", "r") as modelo:
    modelo_lido=modelo.read()
    modelo_pronto=modelo_lido.split(" ")
    for linha in modelo_pronto:
        print(linha) 
          
   
   #função split em ação

'''
def blA():
    with open("junho/modelo.docx", "rb") as modelo:
        modelo_lido=modelo.read()
        modelo_pronto=modelo_lido.replace("  ", "\n")
        print(modelo_pronto)
        for linha in modelo_pronto:
                    print(linha)
      '''          
                
            







