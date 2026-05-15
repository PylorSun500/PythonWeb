from flask import Flask, render_template
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, length, EqualTo
from cursor import insert_user
import datetime
import numpy as np

keygen = np.random.randint(0, 9999999999) 
#似乎有点太简陋了，不过罢了，就问你职能是不是 keygen 吧

app = Flask(__name__)
app.config['SECRET_KEY'] = keygen