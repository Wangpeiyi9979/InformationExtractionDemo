from flask import Flask, render_template, request, jsonify
from utils.findTriple import getTriple
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('Demo.html')

@app.route('/IEDemo', methods=['GET', 'POST'])
def IEDemo():
    text = str(request.args.get("text"))
    print(text)
    ieData = getTriple(text)
    print(ieData)
    return jsonify(ieData)


if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")
