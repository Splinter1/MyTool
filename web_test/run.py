from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/add', methods=['POST'])
def add():
    a = int(request.json['a'])
    b = int(request.json['b'])
    result = a + b
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run()
