from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    namedict = {'person1': 'Alice', 'person2': 'Bob', 'person3': 'Charlie'}
    return render_template('app.html', name = namedict, 
                           paraA = namedict['person1'], 
                           paraB = namedict['person2'], 
                           paraC = namedict['person3'])

if __name__ == '__main__':
    app.run()