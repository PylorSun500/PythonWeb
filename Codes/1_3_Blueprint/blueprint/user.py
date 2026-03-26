'''
此页面是 blueprint 页面的一部分，相对路径位于：
./Codes/1_3_Blueprint/blueprinte

@usage: 教材 P41 的 二.3 题所要求的 user 部分。
'''

from flask import Blueprint
# 实例化蓝图
user_blue = Blueprint("user", __name__)

@user_blue.route('/user')
def user():
    return '这是用户模块。'