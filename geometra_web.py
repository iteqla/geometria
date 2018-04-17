from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return("cazzo funziona!!!!")

@app.route('/geometria', methods=[POST])
def geometria():
    post.create(
        base=request.form['base']
        altezza=request.form['altezza']
    )
    return base*altezza/2

@app.route('/prova')
def prova():
    return "provola"


if __name__ == "__main__":
    app.run(debug=True)