from flask import Flask, render_template, url_for
from forms import FormLogin, FormCriarUsuario, FormRnc

app = Flask(__name__)
app.config['SECRET_KEY'] = '86c033d4458ac3e6f759a6a727d83dbb'

@app.route("/")
def login():
    form_login = FormLogin()
    return render_template("login.html", form_login=form_login)

@app.route("/rnc")
def rnc():
    form_rnc = FormRnc()
    return render_template("rnc.html", form_rnc=form_rnc)

@app.route("/tratativa")
def tratativa():
    return render_template("tratativa.html")

@app.route("/consulta")
def consulta():
    return render_template("consulta.html")

@app.route("/usuarios")
def usuarios():
    form_usuarios = FormCriarUsuario()
    return  render_template("usuarios.html", form_usuarios= form_usuarios)

if __name__=='__main__':
    app.run(debug=True)