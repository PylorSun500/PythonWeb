from flask import Flask, render_template
app = Flask(__name__)

# 书籍列表
@app.route('/books')
def books():
    datetime = '2011-2021'
    msg = '参与出版的书籍'
    books = [
        {'bookname': '计算机基础', 'time': '2011-9-1', 'price': 36}, 
        {'bookname': 'Vue开发教程', 'time': '2013-10-12', 'price': 53},
        {'bookname': 'Python编程入门', 'time': '2015-3-15', 'price': 68},
        {'bookname': 'Flask Web开发实战', 'time': '2017-6-20', 'price': 79},
        {'bookname': '数据结构与算法', 'time': '2018-11-5', 'price': 85},
        {'bookname': '人工智能导论', 'time': '2020-9-30', 'price': 92},
    ]
    return render_template('forbooks.html', **locals()) # **locals() 传递全部的本地变量
# 循环输出九九乘法表
@app.route('/math')
def math():
    return render_template('formath.html')

if __name__ == '__main__':
    app.run(debug=True)