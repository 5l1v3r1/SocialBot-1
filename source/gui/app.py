from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/bots')
@app.route('/bots/')
def bots():
    return render_template('bots.html')
