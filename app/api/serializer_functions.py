from rest_framework.exceptions import ValidationError


def apply_validator(validator, attrs):

    values = [v for v in attrs.values()]
    for value in values:
        validator(str(value))

    return attrs


def validate_special_char(data):
    special_chars = r"\/.,';:!@#$%^&*()_+=-÷≥≤æ…ßå∂≈ç∫´∑åƒ®´˙~`*•"
    for value in data:
        if value in special_chars:
            raise ValidationError('Special character found in a field.')


def validate_email(data):
    special_chars = r"\/,';:!#$%^&*()+=-÷≥≤æ…ßå∂≈ç∫´∑åƒ®´˙~`*•"
    for value in data:
        if value in special_chars:
            raise ValidationError('Special character found in email.')


def validate_age(data):

    if not(data > 18 and data < 100):
        raise ValidationError('Age should be between 18-100.')

def validate_age_type(data):
    if not isinstance(data, int):
        raise ValidationError('Age should be an integer.')
