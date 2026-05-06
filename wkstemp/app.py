from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


app = Flask(__name__)
app.config["SECRET_KEY"] = "abc123"


class LoginForm(FlaskForm):
    username = StringField("用户名", validators=[DataRequired(message="请输入用户名")])
    password = PasswordField(
        "密码",
        validators=[
            DataRequired(message="请输入密码"),
            Length(min=6, message="密码至少6位"),
        ],
    )
    submit = SubmitField("登录")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/form", methods=["GET", "POST"])
def form_demo():
    message = ""
    if request.method == "POST":
        username = request.form.get("username", "")
        hobby = request.form.get("hobby", "")
        message = f"提交成功：姓名是{username}，爱好是{hobby}"
    return render_template("form.html", message=message)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    message = ""
    if form.validate_on_submit():
        message = f"登录成功，欢迎你：{form.username.data}"
    return render_template("login.html", form=form, message=message)


if __name__ == "__main__":
    app.run(debug=True)
