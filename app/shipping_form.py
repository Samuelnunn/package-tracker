from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SelectField, SubmitField
from wtforms.widgets.core import Select
from map.map import map

origin_values = [(k, k) for k in map.keys()]
destination_values = [(k, k) for k in map.keys()]
print(origin_values)


class ShippingForm(FlaskForm):
    sender_name = StringField("Sender Name", [DataRequired()])
    recipient_name = StringField("Recipient Name", [DataRequired()])
    origin = SelectField("Origin", [DataRequired()], choices=origin_values)
    destination = SelectField("Destination", [DataRequired()], choices=destination_values)
    express_shipping = BooleanField("Express Shipping", [DataRequired()])
    submit = SubmitField("Submit")