from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired(message='Este campo é obrigatório.')])
    password = PasswordField('Senha', validators=[DataRequired(message='Este campo é obrigatório.')])
    remember_me = BooleanField('Lembrar de mim')
    submit = SubmitField('Entrar')

class RegistrationForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[
        DataRequired(message='Este campo é obrigatório.'),
        Length(min=4, max=25, message='O nome de usuário deve ter entre 4 e 25 caracteres.')
    ])
    email = StringField('Email', validators=[
        DataRequired(message='Este campo é obrigatório.'),
        Email(message='Por favor, insira um endereço de email válido.')
    ])
    password = PasswordField('Senha', validators=[
        DataRequired(message='Este campo é obrigatório.'),
        Length(min=6, message='A senha deve ter pelo menos 6 caracteres.')
    ])
    password2 = PasswordField('Confirmar senha', validators=[
        DataRequired(message='Este campo é obrigatório.'),
        EqualTo('password', message='As senhas devem ser iguais.')
    ])
    submit = SubmitField('Cadastrar')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Por favor, use um nome de usuário diferente.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Por favor, use um endereço de email diferente.')