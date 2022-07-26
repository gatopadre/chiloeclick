from flask import Flask, render_template, json
from flask_mail import Mail, Message 
import funciones

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.yopmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'gatopadre@yopmail.com'
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

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

@app.route('/catalogo')
def catalogo():
    return render_template(
        'page_catalogo.html', 
        title='Chiloeclick | Catalogo - Encuentra lo que quieres hacer en Chiloe',
        data_locales = funciones.get_data(),)

@app.route('/contacto')
def contacto():
    return render_template('page_contacto.html', title='Chiloeclick | Formulario de Contacto - Dejanos tu mensaje')

@app.route('/contacto/enviar', methods=['POST'])
def enviar_correo_contacto():
    # TODO: falta probar que funcione con un servidor de correo que si funcione
    mensaje = Message(
        "Formulario de contacto", 
        sender='gatopadre@yopmail.com', 
        recipients=['gatopadre@yopmail.com'])
    mensaje.html = '<p>parrafo</p>'
    mail.send(mensaje)
    return json.dumps({'return' : True}), 200, {'ContentType': 'application/json'}


if __name__ == '__main__':
    app.run(port=8080, debug=True, host='0.0.0.0')