#Importar la biblioteca de flask
from flask import Flask, redirect, render_template, request, url_for, flash

#Objeto para inicilizar la aplicacion
#1. ruta donde esta los templates o nombre de la carpeta
app = Flask(__name__, template_folder='template')

#Clave secreta de la aplicacion
app.secret_key = 'ESPE'


#Arreglo para almacenar las tareas
lista_tareas = []

#Controlador de la ruta por defecto
# Ingreso de datos por formulario
# Mostras las tareas pendientes
@app.route('/')
def index():
    return render_template('index.html', lista_tareas=lista_tareas)


#Controlador para enviar los datos
@app.route('/enviar', methods=['POST'])
def enviar():
    if request.method == 'POST':

        t_descripcion = request.form['t_descripcion']
        t_responsable = request.form['t_responsable']
        t_correo = request.form['t_correo']
        t_prioridad = request.form['t_prioridad']


        if t_descripcion == '' or t_correo == '':
            flash('ERROR LLENAR TODOS LOS CAMPOS')
            return redirect(url_for('index'))
        else:

            flash('TAREA AGREGADA')

            lista_tareas.append({'t_descripcion': t_descripcion, 't_responsable': t_descripcion,'t_correo': t_correo, 't_prioridad': t_prioridad })

            return redirect(url_for('index'))

#Controlador de la ruta para borrar
@app.route('/borrar', methods=['POST'])
def borrar():
    if request.method == 'POST':
        
        if lista_tareas == []:

            flash('NO EXISTEN TAREAS')
            return redirect(url_for('index'))

        else:
            lista_tareas.clear()
            flash('TAREAS BORRADAS')
            return redirect(url_for('index'))


#Metodo para correr la aplicacion
if __name__ == '__main__':
    app.run(debug=True)