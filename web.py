from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
import json
app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
Bootstrap(app)


@app.route('/user/<name>')
def index(name):
    return render_template('home.html', title_name='welcome', name=name)


@app.route('/home/<name>')
def home(name):
    return render_template('home.html', title_name='welcome', name=name)


@app.route('/group19')
def group():
    return '<h1>Building</h1>'


@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        data = {'Temperature': request.form['Temperature'], 'Step': request.form['Step'], 'Fat': request.form['Fat']}
        global data
    if request.method == 'GET':
        return json.dumps(data)


@app.route('/data_temperature', methods=['POST', 'GET'])
def data_temperature():
    return jsonify({'Temperature': data['Temperature']})


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)
