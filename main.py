from flask import Flask, render_template, json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', title='Chiloeclick | Home - Turismo en Chiloe, Tours, Cabañas, Hotel')

if __name__ == '__main__':
    app.run(port=8080, debug=True, host='0.0.0.0')