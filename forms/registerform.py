from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length

class contactusform(FlaskForm):
    firstname = StringField(
        validators=[
            InputRequired(),
            Length(min=4, max=200),
        ],
        render_kw={"placeholder": "Nombre"},
    )
    
    lastname = StringField(
        validators=[
            InputRequired(),
            Length(min=4, max=200),
        ],
        render_kw={"placeholder": "Apellido"},
    )
    
    email = StringField(
        validators=[
            InputRequired(),
            Length(min=4, max=200),
        ],
        render_kw={"placeholder": "Email"},
    )
    
    message = StringField(
        validators=[
            InputRequired(),
            Length(min=4, max=300),
        ],
        render_kw={"placeholder": "Mensaje"},
    )

    submit = SubmitField("register")
