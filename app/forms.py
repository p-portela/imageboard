from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, regexp


class PostForm(FlaskForm):
    email = StringField('E-mail')
    subject = StringField('Subject', validators=[Length(min=0, max=100)])
    comment = TextAreaField('Comment', validators=[Length(min=0, max=1000), DataRequired()])
    image = FileField('Image', validators=[DataRequired(), regexp('^.*\.(jpg|JPG|gif|GIF|png|PNG|jpeg|JPEG)$')])
    password = PasswordField('Password')
    submit = SubmitField('Sign In')
