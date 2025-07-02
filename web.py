
filmes={
    "drama": ["Ainda Estou Aqui","O Poderoso Chefão", "Ela"],
    "comédia": ["Tempos Modernos","American Pie","Dr. Dolittle"],
    "policial": ["O Exterminador do Futuro","O Procurado","Velozes e Furiosos"],
    "guerra": ["Rambo","1917","Até o Último Homem"],
    "series":["Stranger things","the boys","gen v","the oficce","attack on titan","the flash","Arcane","Dragon ball GT","La Casa de Papel","Paradise"]
}
página=open("filmes.html","w", encoding="utf-8")
página.write("""
<!DOCTYPE html>
    <html lang="pt-BR">
        <head>
        <meta charset="utf-8">
        <title>Filmes</title>
             <style>
             h1{
    color: black;
}
h2{
    color: rgb(66, 62, 62);
    background-color: rgb(235, 235, 235);
}
             </style>
        </head>
        <body> 
""")
for c, v in filmes.items():
    página.write("<h1>%s</h1>"% c)
    for e in v:
        página.write("<ul><li>%s</li></ul>" % e)

página.write("""
</body>
</html>
""")
página.close()
