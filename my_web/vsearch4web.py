from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return "xxixixishenma"


@app.route('/gg')
def hello1() -> str:
    return "xxixixishenma111111"

app.run()