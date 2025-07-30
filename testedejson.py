import json
def bla():
    dados='{"nome": "Ana", "idade": 25, "ativo": true}'
    dadosemJson=json.loads(dados)
    print(dadosemJson)

dados={"nome": "Ana", "idade": 25, "átivo": True}
with open("dados.json","w", encoding="utf-8") as arquivo:
    json.dump(dados,arquivo,ensure_ascii=True, indent=4)