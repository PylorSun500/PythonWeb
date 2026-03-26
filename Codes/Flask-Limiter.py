# 使用 BaseConverter 进行自定义限制器。
from flask import Flask

from werkzeug.routing import BaseConverter
app = Flask(__name__)

class LetterNumberConverter(BaseConverter):
    regex = '^[a-zA-Z0-9]+$'
app.url_map.converters["letter"] = LetterNumberConverter

@app.route("/<letter:letter>")
def index(letter):
    return f'字母为：{letter}'

if __name__ == '__main__':
    app.run()
