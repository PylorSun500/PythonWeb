from flask import Flask, render_template, request, session, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != '123':
            flash('用户名或密码错误！', category = 'error')
        else:
            session['username'] = request.form['username']
            session['password'] = request.form['password']
            flash('登录成功！', category = 'success')
            return redirect(url_for('homepage'))
    return render_template('login.html')

@app.route('/homepage')
def homepage():
    return render_template('home_page.html')

if __name__ == '__main__':
    app.run(debug=True)