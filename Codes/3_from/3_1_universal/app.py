from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange, ValidationError
import re #正则表达式模块o
from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc'

# 用户注册表单
class RegisterForm(FlaskForm):
    username = StringField(label='手机号', default='')
    email=StringField(label="邮箱",validators=[DataRequired('请输入邮箱'),Length(6,20),Email('请输入正确的邮箱地址')])
    password = PasswordField(label='密码', validators=[DataRequired('请输入密码')])
    conpwd=PasswordField(label='确认密码', validators=[DataRequired('请再次输入密码'),
                                                       EqualTo('password',message="两次密码不一致")])
    age = IntegerField(label='年龄',validators=[NumberRange(min=18,max=50)])
    submit = SubmitField('注册')

    # 自定义验证方法
    def validate_username(self, field):
        """ 验证用户名 """
        # 强制验证用户名为手机号
        username= field.data
        pattern = r'^1[0-9]{10}$' #正则表达式
        if not re.search(pattern, username):
            raise ValidationError('请输入正确的手机号码')
        return field

@app.route("/register",methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return '注册成功！'
    else:
        # 打印错误信息
        print(form.errors)
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run()