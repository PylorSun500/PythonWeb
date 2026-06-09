from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pylor520@localhost:3306/flask_data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    def __repr__(self):
        return f'<User {self.id}: {self.name}>'


@app.route("/")
def add_users():
    user1 = User(name='小明')
    user2 = User(name='小张')
    user3 = User(name='小红')
    db.session.add_all([user1, user2, user3])
    db.session.commit()
    return "OK"


@app.route('/users')
def list_users():
    users = User.query.all()
    print(users)
    id_user = User.query.get(2)
    print(id_user)
    return "OK"


if __name__ == '__main__':
    app.run()
