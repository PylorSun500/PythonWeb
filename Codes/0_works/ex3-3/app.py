# from flask import Flask,render_template
# app=Flask(__name__)
# @app.route("/")
# @app.route("/temp1")
# def temp1():
#     return render_template("temp1-1.html")

# @app.route("/temp2")
# def temp2():
#     return render_template("temp1-2.html")

# if __name__ == '__main__':
#     app.run()

from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# 传递当前页面信息给所有模板
@app.context_processor
def inject_current():
    return {
        'current_path': request.path,
        'current_date': datetime.now().strftime('%Y年%m月%d日')
    }

@app.route("/")
@app.route("/temp1")
def temp1():
    return render_template("temp1-1.html", 
                         page_title="最新文件",
                         active_nav="home",
                         active_tab="temp1")

@app.route("/temp2")
def temp2():
    return render_template("temp1-2.html",
                         page_title="公告公示", 
                         active_nav="home",
                         active_tab="temp2",
                         notice_count=15)

@app.route("/temp3")
def temp3():
    return render_template("temp1-3.html",  # 需要创建这个文件
                         page_title="教育部简报",
                         active_nav="home",
                         active_tab="temp3")

if __name__ == '__main__':
    app.run(debug=True)