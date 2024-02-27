from flask_wft import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email

class RegisterForm(FlaskForm):
    """Register/Create a new user"""

    username = StringField(
        "Username", 
        validators=[InputRequired(), Length(min=1, max=20)]
        )
    password = PasswordField(
        "Password", 
        validators=[InputRequired(), Length(min=6, max=55)]
        )
    email = StringField(
        "Email", 
        validators=[InputRequired(), Email(), Length(max=50)]
        )
    first_name = StringField(
        "Firstname", 
        validators=[InputRequired(), Length(max=30)]
        )
    last_name = StringField(
        "Lastname", 
        validators=[InputRequired(), Length(max=30)]
        )
    

class LoginForm(FlaskForm):
    """Login Form"""

    username = StringField(
        "Username", 
        validators=[InputRequired(), Length(min=1, max=20)]
        )
    password = PasswordField(
        "Password", 
        validators=[InputRequired(), Length(min=6, max=55)]
        )


class FeedbackForm(FlaskForm):
    """Add feedback form."""

    title = StringField(
        "Title",
        validators=[InputRequired(), Length(max=100)],
        )
    content = StringField(
        "Content",
        validators=[InputRequired()],
        )

    
class DeleteForm(FlaskForm):
    """Delete form -- this form is intentionally blank."""
