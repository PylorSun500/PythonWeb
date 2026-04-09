import random
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<score>')
def index(score):
    score_int = int(score)
    return render_template('if.html', score = score_int)

if __name__ == '__main__':
    app.run()