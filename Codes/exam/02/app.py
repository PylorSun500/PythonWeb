string = '    and try and your and best!  and   '
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/test')
def index():
    return render_template('test.html', string=string)

@app.template_filter('cut_and')
def cut_str(data):
    data = data.replace('and', '')
    return data.strip()

if __name__ == '__main__':
    app.run()
