from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, TextField
from wtforms.validators import DataRequired, ValidationError
from flask_wtf.recaptcha.fields import RecaptchaField


# Registration form

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


# Login form

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    recaptcha = RecaptchaField()

# Recipe Form


class RecipeForm(FlaskForm):
    recipe_name = StringField('Recipe Name', validators=[DataRequired()])
    recipe_image = StringField(
        'Enter Image Address Link',
        validators=[
            DataRequired()])
    ingredients = StringField('Enter Ingredients', validators=[DataRequired()])
    recipe_course = StringField(
        'Choose Main, Starter or Desert',
        validators=[
            DataRequired()])
    allergen = StringField(
        'Choose None, Nuts or Eggss',
        validators=[
            DataRequired()])
    serving_size = IntegerField('Serving Size', validators=[DataRequired()])
    calories = IntegerField('Calories', validators=[DataRequired()])
    description = TextField('Enter Description', validators=[DataRequired()])
    cooking_time = IntegerField('Cooking Time', validators=[DataRequired()])
    instruction = TextField('Enter Instruction 1')
    instruction1 = TextField('Enter Instruction 2')
    instruction2 = TextField('Enter Instruction 3')
    instruction3 = TextField('Enter Instruction 4')
    instruction4 = TextField('Enter Instruction 5')
    instruction5 = TextField('Enter Instruction 6')
    instruction6 = TextField('Enter Instruction 7')
    recaptcha = RecaptchaField()
