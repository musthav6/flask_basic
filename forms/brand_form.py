from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class BrandForm(FlaskForm):
    logo = StringField('Logo URL', validators=[DataRequired(), Length(max=255)])
    name = StringField('Brand Name', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    internal_id = StringField('Internal ID', validators=[DataRequired(), Length(max=50)])
    submit = SubmitField('Add Brand')
