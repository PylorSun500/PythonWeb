'''
此页面是 blueprint 页面的一部分，相对路径位于：
./Codes/1_3_Blueprint/blueprinte

@usage: 教材 P41 的 二.3 题所要求的 discuss 部分。
'''

from flask import Blueprint
discuss_blue = Blueprint("discuss", __name__)

@discuss_blue.route('/discuss')
def discuss():
    return '欢迎来到讨论串！'
@discuss_blue.route('/discuss/<id>')
def discussid(id):
    return "议题 {}".format(id)