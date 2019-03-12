from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
# from flask_wtf.recaptcha import RecaptchaField
#
# RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
# RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Regexp('^.{6,10}$', message='Your password should be between 6 and 10 characters long')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    # recaptcha = RecaptchaField()
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Login')

class CheckoutForm(FlaskForm):
    Name_on_card = StringField('Name on Card', validators=[DataRequired(), Length(min=3, max=100)])
    Card_number = StringField('Card Number', validators=[DataRequired(), Length(min=16, max=16)])
    Date = StringField('Expiration date(mm/yyyy)', validators=[DataRequired(), Length(min=7, max=7)])
    Security_num = StringField('Secuity Number', validators=[DataRequired(), Length(min=3, max=3)])

def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user:
        raise ValidationError('This email is already registered.\ please choose a differnt one')

def validate_Username(self, username):
    user = User.Query.filter_by(username=username.data).first()
    if user:
        raise ValidationError('This username is alreadt taken\ Please choose a differnt one')
