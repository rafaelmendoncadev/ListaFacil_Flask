from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, FloatField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Optional, NumberRange

class ListForm(FlaskForm):
    name = StringField('Nome da Lista', validators=[
        DataRequired(message='Este campo é obrigatório.'),
        Length(min=1, max=100, message='O nome deve ter entre 1 e 100 caracteres.')
    ])
    description = TextAreaField('Descrição', validators=[
        Optional(),
        Length(max=500, message='A descrição deve ter no máximo 500 caracteres.')
    ])
    category = StringField('Categoria', validators=[
        Optional(),
        Length(max=50, message='A categoria deve ter no máximo 50 caracteres.')
    ])
    submit = SubmitField('Criar Lista')

class ItemForm(FlaskForm):
    name = StringField('Nome do Item', validators=[
        DataRequired(message='Este campo é obrigatório.'),
        Length(min=1, max=100, message='O nome deve ter entre 1 e 100 caracteres.')
    ])
    category_id = SelectField('Categoria', coerce=int, validators=[Optional()])
    quantity = FloatField('Quantidade', validators=[
        Optional(),
        NumberRange(min=0.1, message='A quantidade deve ser maior que 0.')
    ])
    unit = SelectField('Unidade', choices=[
        ('unidade', 'Unidade'),
        ('kg', 'Kg'),
        ('g', 'Gramas'),
        ('litros', 'Litros'),
        ('ml', 'ML'),
        ('pacote', 'Pacote'),
        ('caixa', 'Caixa')
    ], default='unidade')
    estimated_price = FloatField('Preço Estimado', validators=[
        Optional(),
        NumberRange(min=0, message='O preço deve ser maior ou igual a zero.')
    ])
    notes = TextAreaField('Observações', validators=[
        Optional(),
        Length(max=500, message='As observações devem ter no máximo 500 caracteres.')
    ])
    submit = SubmitField('Adicionar Item')

class CategoryForm(FlaskForm):
    name = StringField('Nome da Categoria', validators=[
        DataRequired(message='Este campo é obrigatório.'),
        Length(min=1, max=50, message='O nome deve ter entre 1 e 50 caracteres.')
    ])
    color = StringField('Cor', validators=[
        Optional(),
        Length(min=7, max=7, message='A cor deve estar no formato hexadecimal (#RRGGBB).')
    ])
    submit = SubmitField('Adicionar Categoria')