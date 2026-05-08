from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
import os
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, FileField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# 配置上传文件夹
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'  # 在生产环境中应该使用更安全的密钥
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 限制上传文件大小为16MB

# 确保上传文件夹存在
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """检查文件扩展名是否允许"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class RegistrationForm(FlaskForm):
    """注册表单类"""
    username = StringField(
        label='用户名',
        validators=[
            DataRequired(message='用户名不能为空'),
            Length(min=3, max=20, message='用户名长度必须在3-20个字符之间')
        ],
        render_kw={
            'placeholder': '请输入用户名',
            'required': 'true'
        }
    )
    
    email = EmailField(
        label='邮箱',
        validators=[
            DataRequired(message='邮箱不能为空'),
            Email(message='请输入有效的邮箱地址')
        ],
        render_kw={
            'placeholder': '请输入邮箱地址',
            'required': 'true'
        }
    )
    
    password = PasswordField(
        label='密码',
        validators=[
            DataRequired(message='密码不能为空'),
            Length(min=6, max=20, message='密码长度必须在6-20个字符之间')
        ],
        render_kw={
            'placeholder': '请输入密码',
            'required': 'true'
        }
    )
    
    confirm_password = PasswordField(
        label='确认密码',
        validators=[
            DataRequired(message='请确认密码'),
            EqualTo('password', message='两次输入的密码不一致')
        ],
        render_kw={
            'placeholder': '请再次输入密码',
            'required': 'true'
        }
    )
    
    avatar = FileField(
        label='头像上传',
        validators=[DataRequired(message='请选择要上传的文件')]
    )
    
    submit = SubmitField('注册')

@app.route('/')
def index():
    """首页路由"""
    return '<h1>欢迎来到注册页面示例！</h1><p><a href=" ">点击注册</a ></p >'

@app.route('/register', methods=['GET', 'POST'])
def register():
    """注册页面路由"""
    form = RegistrationForm()
    
    if form.validate_on_submit():

        username = form.username.data
        email = form.email.data
        password = form.password.data
        
    
        file = form.avatar.data
        if file and allowed_file(file.filename):
            # 使用secure_filename确保文件名安全
            filename = secure_filename(file.filename)
            # 保存文件到上传文件夹
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash(f'用户 {username} 注册成功！头像已上传。', 'success')
            return redirect(url_for('index'))
        else:
            flash('文件类型不被允许，请上传以下格式的文件：txt, pdf, png, jpg, jpeg, gif', 'error')
    
    return render_template('register.html', form=form)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """提供上传文件的访问"""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)