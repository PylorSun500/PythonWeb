'''
操作数据表
'''
from app import app
from app import db
from model import Student

"""
5.4.1 增加数据
"""
@app.route("/add")
def add_data():
    # 创建Student类的对象
    student1 = Student(name="小明", gender='男', teacher='李越')
    student2 = Student(name="小张", gender='男', teacher='李越')
    student3 = Student(name="小红", gender='女', teacher='李越')
    # 将Student类的对象添加到数据库会话中
    db.session.add_all([student1, student2, student3])
    # 使用commit()方法从会话提交至数据库
    db.session.commit()
    return "学生数据添加成功！"

"""
5.4.2	查询数据
"""
@app.route("/check")
def check_data():
    # 查询语句的格式： 模型类.query.<过滤方法>.<查询方法>

    # 返回主键值所对应的记录
    student1 = db.session.get(Student, 1)
    print(student1)
    student2 = db.session.get(Student, 2)
    print(student2)
    return (f'数据查询成功! \n '
            f'{student1.name}的性别为{student1.gender} \n '
            f'{student2.name}的性别为{student2.gender}')

"""
5.4.3	更新数据
"""
@app.route("/update")
def update_data():
    # 返回主键值2对应的记录
    result = db.session.get(Student, 3)
    print(result.teacher)
    # 将username的值修改为"小兰"
    result.teacher = "小兰"
    db.session.commit()
    return "数据更新成功！"

if __name__ == '__main__':
    app.run()
