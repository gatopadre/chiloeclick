from flask import Flask, render_template, json

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', title='Chiloeclick | Home - Turismo en Chiloe, Tours, Cabañas, Hotel')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html', title='Chiloeclick | Nosotros - Mision y Vision')

@app.route('/suscripciones')
def suscripciones():
    return render_template('suscripciones.html', title='Chiloeclick | Suscripciones a Chiloeclick - Elije tu plan')

@app.route('/recomendaciones')
def recomendaciones():
    return render_template('recomendaciones.html', title='Chiloeclick | Recomendaciones - ')

@app.route('/contacto')
def contacto():
    return render_template('contact.html', title='Chiloeclick | Formulario de Contacto - Dejanos tu mensaje')

if __name__ == '__main__':
    app.run(port=8080, debug=True, host='0.0.0.0')