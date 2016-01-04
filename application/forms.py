from wtforms import BooleanField, TextField, PasswordField, validators, IntegerField, SelectField, TextAreaField, RadioField
from wtforms.widgets import TextArea
from wtforms.fields.html5 import DateField, DateTimeField
from wtforms.validators import DataRequired, ValidationError, NumberRange, Email
from flask.ext.wtf import Form

class TicketForm(Form):
    project = SelectField('Project', choices=[('Unknown', 'Unknown'), ('CF', 'CF'), ('DMP', 'DMP'), ('LC', 'LC')], default='Unknown')
    title = TextField('Title', [validators.Length(min=1, max=200)])
    description = TextAreaField('Description', [validators.Length(min=1, max=500)])
    contact = TextField('Contact Name', [validators.Length(min=0, max=200)])
    priority = RadioField('Priority', choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Low')
