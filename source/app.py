from flask import Flask, render_template, request
from api.api import API, APIError


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/apps')
def apps():
    return render_template('apps.html')


@app.route('/bot')
def bot():
    return render_template('bot.html')


@app.route('/api')
@app.route('/api/')
def api_no_command():
    return APIError.create(message='No api command found.', code=400)


@app.route('/api/<cmd>', methods=['GET', 'POST'])
def handle_request(cmd=None):
    cmds = {
        'test': API.test,
        'bot': API.bot,
        'config': API.config
    }

    func = cmds.get(cmd, lambda request: APIError.create(message='Could not find command ' + cmd, code=400))
    return func(request=request)


@app.route('/<url>')
def catch_all(url=None):
    return render_template('404.html', url=url)

