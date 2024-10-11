from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)
@app.route('/')
def say_hello():
    return "<p>Hello!</p>"
@app.route('/hello') 
def hello(): 
    tekst = """
    <head>
    <style> 
    p {color:red;}
    </style>
    </head>
    <body>  
    <h1>To jest strona HELLO</h1>
    <p>NKONKONISONII</p> 
    </body>        """
    return tekst
@app.route('/path/<path:y>')
def pathy(y):
    x = y.lower()
    return f"<h2 style='color: red'>sciezka = {x}</h2>"
@app.route('/calc/<int:zm1>')
def calc(zm1):
    return f"{zm1} * 10 = {zm1 * 10}"
@app.route('/Result')
def about(): 
    return render_template('about.html')
@app.route('/tree')
def drzewo():
    return render_template('drzewo.html')
@app.route('/user/<username>')
def user(username):
    y = "Patryk"
    x = username.upper()
    if f"{username}" == y : 
        return f"<h1>Witaj Administratorze</h1>"
    else: 
        return f"<h2>CZesc {escape(x)}</h2>"