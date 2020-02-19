# make websites with python: https://flask.palletsprojects.com/en/1.1.x/quickstart/

from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
########    # write you code between the hastags #########

    L = ['cat', 'dog', 'fish', 'frogs', 'snake']


########    # write you code between the hastags #########
    return render_template('index.html', L = L)


if __name__ == '__main__':
    app.run(debug=True)
