from django.core.exceptions import ValidationError


def is_greater_than_zero(value: float):
    if value <= 0:
        raise ValidationError(
            ("%(value)s is not a greater than zero value"),
            params={"value": value},
        )

def valid_if_value_is_positive(value: float):
    if value < 0:
        raise ValidationError(
            ("%(value)s is not positive value"),
            params={"value": value},
        )