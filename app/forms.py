from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Length

class OperatorAnalysis(FlaskForm):
    regulator_accession = StringField("Regulator Accession", validators=[DataRequired()])
    operator_sequence = StringField("Operator Sequence", validators=[DataRequired()])

class RegulatorAnalysis(FlaskForm):
    regulator_accession = StringField("Regulator Accession", validators=[DataRequired()])

