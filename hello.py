from flask import Flask, render_template
from flask_bootstrap import Bootstrap
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


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)
