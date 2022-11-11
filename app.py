from flask import Flask
from flask import request
from flask import render_template 

app = Flask(__name__)
 

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/usuario/<name>/<options>')
def user(name, options):
    print(name, options)
    return render_template("user.html", name = name)

@app.route('/navegador')
def browser():
    user_agent = request.headers.get("User-Agent")
    return f"tu navegador es: {user_agent}"

@app.route('/rutas') 
def routes():
    print(app.url_map)
    return "revisa tu consola para ver las rutas"