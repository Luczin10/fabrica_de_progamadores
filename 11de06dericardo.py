
          
tarefas_concluidas={"dar aula": "tarefa concluido","viver por mais um dia": "tarefa concluida" }
tarefas_não_concluidas={"dar doçes para os alunos": "não concluido", "comprar uma ferrari": "não concluido"}
tarefas_em_geral=tarefas_concluidas,tarefas_não_concluidas
while True:
    escolha=int(input("Oque deseja fazer?   1-adicionar tarefa      2-remover tarefa        3-visualizar tarefa     4-sair"))
    if escolha==4:
        print("Cabô")
        break
    if escolha==1:
        tarefa=input("Qual a tarefa?")
        resposta=int(input("é uma tarefa concluida ou não 1-concluida   2-não concluida"))
        if resposta==1:
            tarefas_concluidas[tarefa]="concluida"
            print(tarefas_concluidas)
        else:
            tarefas_não_concluidas[tarefa]="não concluida"
            print(tarefas_não_concluidas)
            
    elif escolha==3:
        print(tarefas_em_geral)
    elif escolha==2:
              resposta=int(input("é uma tarefa concluida ou não 1-concluida   2-não concluida"))
            if resposta==1:
                tarefa_remove=input("Digite qual tarefa ira retirar").lower()
                del tarefas_concluidas[tarefa_remove]
            else:
                tarefa_remove=input("Digite qual tarefa ira retirar").lower()
                del tarefas_não_concluidas[tarefa_remove]
    else:
        print("erro")
        break


        
