# 导入Flask-SQLAlchemy扩展库，这是一个强大的Python SQL工具包和对象关系映射(ORM)库
from flask_sqlalchemy import SQLAlchemy

# 创建SQLAlchemy实例，用于ORM操作
db = SQLAlchemy()

class WaterSystem(db.Model):
    """
    江西五大水系数据模型

    用于存储和管理水系的基本信息，包括名称、水位、文化介绍和图片路径等。
    继承自db.Model，对应数据库表'water_systems'。

    Attributes:
        __tablename__ (str): 数据库表名
        id (int): 水系唯一标识符
        name (str): 水系名称
        water_level (float): 实时水位(米)
        culture_intro (str): 富有温度的文化简介
        image_path (str): 本地图片相对路径
    """
    __tablename__ = 'water_systems'  # 指定数据库表名为'water_systems'
    id = db.Column(db.Integer, primary_key=True)  # 定义id字段，整数类型，为主键
    name = db.Column(db.String(50), nullable=False, comment='水系名称')  # 定义name字段，字符串类型，长度50，不能为空，表示水系名称
    water_level = db.Column(db.Float, comment='实时水位(米)')  # 定义water_level字段，浮点类型，表示实时水位，单位为米
    culture_intro = db.Column(db.Text, comment='富有温度的文化简介')  # 定义culture_intro字段，文本类型，存储富有温度的文化简介
    image_path = db.Column(db.String(200), comment='本地图片相对路径')  # 定义image_path字段，字符串类型，长度200，存储本地图片的相对路径