
from flask import Flask, request, render_template
from controllers.citaController import crearCita, verCitas
from controllers.doctorController import verDoctor
from controllers.enfermeroController import verEnfermero

app = Flask(__name__)


@app.route('/citas', methods=['GET'])
def formulario():
    return render_template('Cita.html')  

@app.route('/doctores', methods=['GET'])
def pagina_doctores():
    doctores = verDoctor()
    return render_template('doctores.html', doctores=doctores)

@app.route('/', methods=['GET'])
def homepage():
    return render_template('home.html')


@app.route('/enfermeros')
def mostrar_enfermeros():
    enfermeros = verEnfermero()
    print(enfermeros)
    return render_template('enfermeros.html', enfermeros=enfermeros)

@app.route('/citas', methods=['POST'])
def agregar_cita():
    if request.method == 'POST':
        nombre = request.form['nombre']
        fecha = request.form['fecha']
        hora = request.form['hora']
        motivo = request.form['motivo']
        
        respuesta = crearCita(nombre, fecha, hora, motivo, "Pendiente")
        
        if respuesta:
            return render_template('home.html')
        else:
            return 'Error al crear cita'
        
@app.route('/mis-citas', methods=['GET'])
def ver_citas():
    citas = verCitas()
    print(citas)
    return render_template('mis_citas.html', citas=citas)

if __name__ == '__main__':
    app.run(debug=True)
