from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SelectField
from wtforms.widgets.core import Select
from map.map import map

class ShippingForm(FlaskForm):
    sender_name = StringField("Sender Name", [DataRequired()])
    recipient_name = StringField("Recipient Name", [DataRequired()])
    origin = SelectField("Origin", [DataRequired()])
    destination = SelectField("Destination", [DataRequired()])
    express_shipping = BooleanField("Express Shipping",[DataRequired()])
    