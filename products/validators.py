from django.core.exceptions import ValidationError
from datetime import datetime


# raise errorlar
def validate_timestamp(value):
    today = datetime.now().date()

    # eger bu gunki tarixden evvelki tarixdirse
    if value < today:
        raise ValidationError("balamsan vaxti indiden evvel qeyd etme")
