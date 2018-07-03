from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
import mycsv as csv
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


@app.route('/home/<name>/temperature')
def temperature(name):
    return render_template('temperature.html', title_name='temperature', name=name)


@app.route('/home/<name>/step')
def step(name):
    return render_template('step.html', title_name='step', name=name)


@app.route('/home/<name>/fat')
def fat(name):
    return render_template('fat.html', title_name='fat', name=name)


@app.route('/group19')
def group():
    return '<h1>Building</h1>'


@app.route('/data', methods=['GET', 'POST'])
def data_get():
    global data
    if request.method == 'POST':
        data = {'Temperature': request.form['Temperature'], 'Step': request.form['Step'], 'Fat': request.form['Fat']}
    if request.method == 'GET':
        return json.dumps(data)


@app.route('/data_temperature', methods=['POST', 'GET'])
def data_temperature():
    return jsonify({'Temperature': data['Temperature']})


@app.route('/data/raw')
def data_get_EEG_raw():
    global EEG_raw_data, counter_raw
    counter_raw += 1
    if counter_raw > 15000:
        counter_raw = 0
    return jsonify({'Raw': str(EEG_raw_data[counter_raw])})


@app.route('/data/eeg')
def data_get_EEG_all():
    global EEG_all_data, counter_EEG
    counter_EEG += 1
    if counter_EEG > 31:
        counter_EEG = 0
    return jsonify({'Delta': str(EEG_all_data[counter_EEG][3]),
                    'Theta': str(EEG_all_data[counter_EEG][4]),
                    'LowAlpha': str(EEG_all_data[counter_EEG][5]),
                    'HigAlpha': str(EEG_all_data[counter_EEG][6]),
                    'LowBeta': str(EEG_all_data[counter_EEG][4]),
                    'HighBeta': str(EEG_all_data[counter_EEG][4]),
                    'LowGamma': str(EEG_all_data[counter_EEG][4]),
                    'MidGamma': str(EEG_all_data[counter_EEG][4])})


@app.route('/data/ecg')
def data_get_ECG():
    global ECG_data, counter_ECG
    counter_ECG += 5
    if counter_ECG > 4000:
        counter_ECG = 0
    return jsonify({'ECG': str(ECG_data[counter_ECG])})


if __name__ == '__main__':
    data = {'Temperature': 36.8, 'Step': 1999, 'Fat': 9.1}
    counter_raw = -1
    counter_EEG = -1
    counter_ECG = -1
    EEG_raw_data = csv.raw_reader()
    EEG_all_data = csv.EEG_reader()
    ECG_data = csv.ECG_reader()
    app.run("0.0.0.0", port=30000, debug=True)
