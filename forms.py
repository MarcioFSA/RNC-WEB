from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class FormLogin(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6,20)])
    botao_login = SubmitField('Fazer Login')
    botao_anonimo = SubmitField('Anônimo')

class FormCriarUsuario(FlaskForm):
    nome = StringField('Nome Completo', validators=[DataRequired()])
    usuario = StringField('Usuario', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    perfil = SelectField('Perfil - Colocar A ComboBox')

class FormRnc(FlaskForm):
    setor_registro = StringField('Setor de Registro - Colocar combobox', validators=[DataRequired()])
    setor_ocorrencia = StringField('Setor de Ocorrencia da Não Conformidade - ComboBox', validators=[DataRequired()])
    nao_conformidade = StringField('Não conformidade - ComboBox', validators=[DataRequired()])
    descricao = TextAreaField('Descreva a Não Conformidade', validators=[DataRequired()])
    turno = BooleanField('SN ou MT', validators=[DataRequired()])
