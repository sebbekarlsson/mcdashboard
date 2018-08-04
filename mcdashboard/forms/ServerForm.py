from wtforms import Form, StringField, IntegerField, validators


class ServerForm(Form):
    name = StringField('Name', [validators.Length(max=120)])
    port = IntegerField('Port')
