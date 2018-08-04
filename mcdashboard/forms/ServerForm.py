from wtforms import Form, StringField, validators


class ServerForm(Form):
    name = StringField('Name', [validators.Length(max=120)])
