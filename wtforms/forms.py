from wtforms import Form, StringField, TextAreaField, validators

class MyFrom(Form):
    name = StringField('Name', [validators.DataRequired()])
    email = StringField('Email', [validators.DataRequired()])
    message = TextAreaField('Message', [validators.DataRequired()])
