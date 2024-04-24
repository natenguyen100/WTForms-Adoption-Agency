from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, URL, Optional, NumberRange

class AddPet(FlaskForm):
    name = StringField("Name of Pet", validators=[InputRequired()])
    species = SelectField("Species", choices=[("cat", "cat"), ("dog", "dog"), ("porcupine", "porcupine")])
    photo_url = StringField("Photo Url", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes", validators=[Optional()])

class EditPet(FlaskForm):
    photo_url = StringField("Photo Url", validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available")