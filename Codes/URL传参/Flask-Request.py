# 使用 request.args.get() 控制从 URL 传入的参数。
from flask import Flask, request
app = Flask(__name__)

@app.route("/gettest")
def gettest():
    return "你的姓名为{}，你的年龄为{}".format(request.args.get("name"), \
                                           request.args.get("age"))