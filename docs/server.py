from flask import Flask

app = Flask(__name__)

@app.route("/")
def main_page():
    return open('sources/index.html', "r").read()


@app.route("/model_use")
def model_use():
    return open('model_use.html', "r").read()

@app.route("/predicted_bots")
def predicted_bots():
    return open('predicted.html', "r").read()

@app.route("/explain")
def explain():
    return open('explain.html', "r").read()







