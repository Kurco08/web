# Comandos base para la aplicacion #
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def main():
    return render_template('home.html')
@app.route('/contactos')
def contactos():
    return render_template('contactos.html')
@app.route('/postres')
def postres():
    return render_template('postres.html')
@app.route('/comidas')
def comidas():
    return render_template('comidas.html')
@app.route('/bebidas')
def bebidas():
    return render_template('bebidas.html')
@app.route('/niñosp')
def niñosp():
    return render_template('niñosp.html')
@app.route('/niñosc')
def niñosc():
    return render_template('niñosc.html')
@app.route('/niñosb')
def niñosb():
    return render_template('niñosb.html')
@app.route('/adultosp')
def adultosp():
    return render_template('adultosp.html')
@app.route('/adultosc')
def adultosc():
    return render_template('adultosc.html')
@app.route('/adultosb')
def adultosb():
    return render_template('adultosb.html')
@app.route('/bebidasadulto1')
def bebidasadulto1():
    return render_template('bebidasadulto1.html')
@app.route('/bebidasadulto2')
def bebidasadulto2():
    return render_template('bebidasadulto2.html')
@app.route('/bebidasniños1')
def bebidasniños1():
    return render_template('bebidasniños1.html')
@app.route('/bebidasniños2')
def bebidasniños2():
    return render_template('bebidasniños2.html')
@app.route('/comidasadultos1')
def comidasadultos1():
    return render_template('comidasadultos1.html')
@app.route('/comidasadultos2')
def comidasadultos2():
    return render_template('comidasadultos2.html')
@app.route('/comidasniños1')
def comidasniños1():
    return render_template('comidasniños1.html')
@app.route('/comidasniños2')
def comidasniños2():
    return render_template('comidasniños2.html')
@app.route('/postresadultos1')
def postresadultos1():
    return render_template('postresadultos1.html')
@app.route('/postresadultos2')
def postresadultos2():
    return render_template('postresadultos2.html')
@app.route('/postresniños1')
def postresniños1():
    return render_template('postresniños1.html')
@app.route('/postresniños2')
def postresniños2():
    return render_template('postresniños2.html')
@app.route('/integrantes')
def integrantes():
    return render_template('integrantes.html')
if __name__ == "__main__":
    app.run(host="10.53.4.48", port=5000, debug=True)
