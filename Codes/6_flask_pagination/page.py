from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import random

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@127.0.0.1:3306/flask_data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
# 创建组件对象
db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = "student_test"
    id = db.Column(db.Integer, primary_key=True,comment="主键ID")
    name = db.Column(db.String(250), comment="姓名")
    age = db.Column(db.Integer, comment="年龄")
    sex = db.Column(db.Boolean, default=False, comment="性别")

    def __repr__(self):
        return self.name

@app.route("/add")
def add():
    for i in range(100):
       student=Student(name="student_{}".format(i),age=random.randint(18, 25))
       db.session.add(student)
    db.session.commit()
    return "数据添加"

@app.route("/test")
def test():
    # 1.初步设置页码，默认为1
    page = int(request.args.get('page', 1)) # 获取get请求数据：参数是page、默认值是1、类型是：int
    # 2.查询年龄为20-22之间的结果，准备数据
    query = Student.query.filter(Student.age.between(20, 22))
    # 3.创建pagination对象，page表示当前页码，per_page表示每页显示记录条数
    pagination = query.paginate(page=page, per_page=5, error_out=False)
    # 4.在模板中实现分页展示
    return render_template("student_page.html", pagination=pagination)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    # db.drop_all()
    # db.create_all()
    app.run()

