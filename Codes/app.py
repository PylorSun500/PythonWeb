from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_flask():
    return "Hello, Flask!"
def new_page():
    return "我是孙玮宏嗯对"
# 使用 add_url_rule 注册新路由，也就是做个新的子界面。
app.add_url_rule(rule="/new", view_func=new_page)
if __name__ == '__main__':
    app.run()
