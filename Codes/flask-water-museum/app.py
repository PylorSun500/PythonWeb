from flask import Flask, render_template
from config import Config
from models import db, WaterSystem

# 初始化Flask应用实例
app = Flask(__name__)
# 从配置对象中加载应用配置
app.config.from_object(Config)
# 初始化数据库并绑定到Flask应用
db.init_app(app)

@app.route('/')
@app.route('/index')
def index():
    """
    数字展馆首页

    Returns:
        渲染后的 index.html 模板
    """
    return render_template('index.html')

# ******************************************************
# 【核心全栈数据流】路由 -> 数据库查询 -> 模板渲染
# ******************************************************
@app.route('/water-list')
def water_list():
    """
    数字展馆水系列表页
    全栈数据流三步曲：
    1. 路由匹配：浏览器访问 /water-list 触发本函数
    2. ORM查询：从MySQL获取所有水系数据
    3. 模板传参：通过变量 water_systems 传递给Jinja2
    """
    # ---- 【重点】数据库查询 ----
    # WaterSystem.query.all() 底层生成 SELECT * FROM water_systems
    # 返回所有 WaterSystem 模型实例列表
    water_systems = WaterSystem.query.all()  # 变量命名需与模板严格一致

    # ---- 【重点】模板渲染 ----
    # 左变量名 water_systems 对应模板中 {{ water_systems }} 循环对象
    return render_template('water_list.html', water_systems=water_systems)

if __name__ == '__main__':
    app.run(debug=True)