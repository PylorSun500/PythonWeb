'''
此页面是 blueprint 页面的一部分，相对路径位于：
./Codes/1_3_Blueprint/blueprinte

@usage: 教材 P41 的 二.3 题所要求的 admin 部分。
'''

from flask import Blueprint
admin_blue = Blueprint("admin", __name__)

@admin_blue.route('/admin')
def admin():
    return "管理员登录："