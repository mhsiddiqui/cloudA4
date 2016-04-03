from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class MyForm(Form):
    a = StringField('a', validators=[DataRequired()])
    b = StringField('b')
    c = StringField('c')