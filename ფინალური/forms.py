from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired()]
    )

    email = StringField(
        "Email",
        validators=[DataRequired()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired()]
    )

    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired()]
    )

    submit = SubmitField("Login")
from wtforms import TextAreaField

class MovieForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    year = StringField("Year", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    image = StringField("Image Name", validators=[DataRequired()])

    submit = SubmitField("Save")