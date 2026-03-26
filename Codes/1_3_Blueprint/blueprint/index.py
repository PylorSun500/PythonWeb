from flask import Flask
import admin, discuss, user
appself = Flask(__name__)
@appself.route('/')
def index():
    return '主页面！'

appself.register_blueprint(user.user_blue)
appself.register_blueprint(admin.admin_blue)
appself.register_blueprint(discuss.discuss_blue)

if __name__ == '__main__':
    appself.run()
