import flask
import os

app = flask.Flask(__name__)

@app.route('/') # amikor megnyitja a weboldalt a kezdőoldalon betölti az 'index.html'-t
def home():
    return flask.render_template('index.html')

@app.route('/open_python') # amikor átvált a weboldalon az 'index.html/open_python' oldalra elindítja a 'main.py'-t
def open():
    os.startfile('main.py')
    return ''

if __name__ == '__main__':
    app.run(debug=True,port=5000) # A portot meg lehet változtatni