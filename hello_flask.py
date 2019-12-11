# -*- coding: UTF-8 -*-
"""
hello_flask: First Python-Flask webapp
"""
from flask import Flask, render_template, request # From module flask import class Flask
import pandas as pd
import matplotlib.pyplot as plt
import os

nomimagen=""

app = Flask(__name__) # Construct an instance o Flask class for our webapp

@app.route('/ir_a_sube')
def ir_a_sube_vista():
    return render_template('sube.html')

@app.route('/sube_archivo', methods=['GET','POST'])
def sube():
    print("Algo")
    global nomimagen
    x=""
    tipo=""
    y=""

    nombre=""
    url = ""
    if request.method == 'POST':
        #lee los datos del archivo
        datos = pd.read_csv(request.files.get('file'), delimiter=",")
        x = request.form['x']
        y = request.form['y']
        nombre =request.form["nombre"]
        tipo = request.form["tipo"]
        print(x)
        print(tipo)
        nomimagen=y+'.png'
        imagen = ""
        print(nomimagen)
        if(tipo=='barras'):
            print("entra a barrras")
            datos.head().groupby(x)[y].sum().plot(kind='bar',legend='reverse')
            plt.savefig("static/"+nomimagen)
            print("nombre imagen: ", nomimagen)
            return render_template("mostrar.html")
            #nomimagen=""
        elif(tipo=='lineas'):
            datos.head().groupby(x)[y].sum().plot(kind='line',legend='reverse')
            plt.savefig("static/"+nomimagen)
            print(nomimagen)
            return render_template("mostrar.html")
            #nomimagen=""
        elif(tipo=='pastel'):
            datos.head().groupby(x)[y].sum().plot(kind='pie',legend='reverse')
            #path = '/Imagenes'
            plt.savefig("static/"+nomimagen)
            print(nomimagen)
            return render_template("mostrar.html")
            #nomimagen=""
    return render_template('sube.html',x=x)

@app.route('/mostrar_grafica', methods=['GET','POST'])
def mostrar():
    if request.method == 'POST':
        global nomimagen
        return render_template('grafica.html',  nomimagen=nomimagen)
    return render_template('mostrar.html')


@app.route('/') # URL '/' to be handled by main() route handler
def main():
    """Say hello"""
    return render_template('index.html')


if __name__ == '__main__': # Script executed directly?
    app.run() # Launch built-in web server and run this Flask webapp
