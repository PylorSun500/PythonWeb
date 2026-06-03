"""
连接数据库
此前应在终端中做好数据库和数据表结构的构建
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 连接数据库
# 容器不是 localhost ，不能通过 localhost 连接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root123@mysql/flask_data'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    teacher = db.Column(db.String(20), nullable=False)
    
    # 保证输出格式
    def __repr__(self):
        return f'学生：{self.name}'

"""
增加数据
"""
@app.route("/")
def hello_flask():
    # 创建 User 类的对象
    user1 = User(name = "Pylor", gender = 1, teacher = "李程越")
    user2 = User(name= "Shibetta", gender = 1, teacher = "李程越")
    user3 = User(name="Laura", gender = 0, teacher = "李程越")
    # 将 User 类的对象添加到数据库会话中
    db.session.add_all([user1, user2, user3])
    # 使用 commit() 方法从会话提交至数据库
    db.session.commit()
    return "已经提交！"
if __name__ == "__main__":
    app.run()


"""
5.4.2	查询数据
"""
定义路由及视图函数
@app.route("/")
def hello_flask():
    # 查询全部记录
    users = User.query.all()
    print(users)
    # 查询第一条记录
    first_user = User.query.first()
    print(first_user)
    # 返回主键值 2 对应的记录
    id_user = db.session.get(User, 2)
    print(id_user)
    # 过滤 name 等于 "Jankwan" 的记录（虽然已经不存在了）
    users2 = User.query.filter(User.name == "Jankwan").first()
    print(users2)
    # 过滤 email 等于 "123@qq.com" 的记录
    users3 = User.query.filter_by(gender = 1).first()
    print(users3)
    
    return "查询完成！"
    
if __name__ == "__main__":
    # 先创建表（第一次运行需要）
    with app.app_context():
        db.create_all()
        print("✅ 表已创建")
    
    app.run(host='0.0.0.0', port=5001)

"""
5.4.3	更新数据
"""
@app.route("/")
def hello_flask():
    result = User.query.filter(User.teacher == "李程越").update({"teacher" : "Kexin YI"})
    db.session.commit()
    return "OK"
if __name__ == "__main__":
    app.run()


"""
5.4.4	删除数据
"""
@app.route("/")
def hello_flask():
    # 返回主键值 3 对应的记录
    result = db.session.get(User, 2)
    print(result)
    db.session.delete(result)
    db.session.commit()
    return "OK"

if __name__ == "__main__":
    app.run()