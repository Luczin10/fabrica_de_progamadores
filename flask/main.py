from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def inicial():
    return render_template("index.html")

@app.route('/exemple/')
def exemple():
    a = ""
    print(a)
    return render_template("consulta.html", context=a)
app.run()
