from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtfroms.validators import DataRequired

class LoginFor(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
