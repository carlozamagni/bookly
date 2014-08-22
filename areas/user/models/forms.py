from flask_wtf import Form, RecaptchaField
from wtforms import TextField, PasswordField, HiddenField
from wtforms.validators import DataRequired

__author__ = 'cazamagni'


class RegisterForm(Form):
    first_name = TextField('first_name', validators=[DataRequired()], description={'placeholder': 'first name'})
    last_name = TextField('last_name', validators=[DataRequired()], description={'placeholder': 'last name'})
    user_name = TextField('username', validators=[DataRequired()], description={'placeholder': 'username'})
    email = TextField('email', validators=[DataRequired()], description={'placeholder': 'email'})

    password = PasswordField(validators=[DataRequired()], description={'placeholder': 'password'})
    password_check = PasswordField(validators=[DataRequired()], description={'placeholder': 'retype password'})

    role = HiddenField("user")

    # see: https://flask-wtf.readthedocs.org/en/latest/form.html
    # recaptcha = RecaptchaField()

    '''
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
    '''

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        if self.password.data != self.password_check.data:
            return False

        return True