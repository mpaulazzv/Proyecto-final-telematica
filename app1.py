import flask, jinja2
import pandas as pd
import os
from flask import Flask, render_template, request, flash, url_for, redirect


app1 = flask.Flask(__name__)
app1.secret_key = 'my_secret_key'

loader = jinja2.FileSystemLoader('templates')


@app1.route('/')
def pag_inicio():
    return '<h1>Página de inicio de la red social</h1>'


@app1.route('/crear_usuario', methods=['GET', 'POST'])

def crear_usuario():

    if request.method == 'POST':

        nombre = str(request.form['Nombre'])
        
        password = str(request.form['Contrasena'])
        base_datos_l = open('base_datos.csv', 'r')
        base_datos_w = open('base_datos.csv', 'a')
        base_datos = pd.read_csv('base_datos.csv')
        existe=False
        puerto = 8000

        for i in range (len(base_datos)):
            if nombre == base_datos.iloc[i, 0].split(';')[0]:
                existe = True
                flash('EL usuario ya existe')
                break
        
        if existe == False:

            a=puerto + len(base_datos)
            base_datos_w.write(nombre+";"+password+";"+str(a)+"\n")
            os.system('docker build . -t '+nombre.lower())
            flash('Usuario creado correctamente')
                 
        
        base_datos_w.close()


    return render_template('index.html')

@app1.route('/login', methods=['GET', 'POST'])
def iniciar_sesion():

    if request.method == 'POST':

        nombre = str(request.form['Nombre'])
        password = str(request.form['Contrasena'])
        existe = False
        base_datos = pd.read_csv('base_datos.csv')
        

        for i in range (len(base_datos.index)):
            if nombre == base_datos.iloc[i, 0].split(';')[0] and password == base_datos.iloc[i, 0].split(';')[1]:
                existe = True
                puerto = base_datos.iloc[i, 0].split(';')[2]
                flash('Ha ingresado correctamente, será redirigido a su página')
                break

        if existe == False:
            flash('Credenciales de inicio de sesión incorrectas')
        else:
            os.system('docker run -d -p '+str(puerto)+':80 '+nombre.lower())
            return redirect('http://localhost:'+str(puerto))

    return render_template('login.html')


if __name__ == '__main__':
    app1.run(host='0.0.0.0', port=80)
