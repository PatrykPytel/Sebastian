from flask import Flask, render_template
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