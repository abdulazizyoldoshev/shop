import re
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
import phonenumbers


@deconstructible
class PhoneValidator():
    requires_context = False

    @staticmethod
    def clean(value):
        return re.sub('[^0-9]+', '', value)

    @staticmethod
    def validate(value):
        try:
            z = phonenumbers.parse("+" + value)
            if not phonenumbers.is_valid_number(z):
                return False
        except:
            return False

        if len(value) != 12 or not value.startswith("998"):
            return False

        return True

    @staticmethod
    def format(value):
        try:
            z = phonenumbers.parse("+" + value)
            if not phonenumbers.is_valid_number(z):
                return value

            return phonenumbers.format_number(z, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        except:
            return value

    def call(self, value):
        if not PhoneValidator.validate(value):
            raise ValidationError("Kiritilgan qiymat telefon raqami emas.")


@deconstructible()
class MyValidators():
    def __call__(self, value):
        if value.startswith('Hi'):
            return
        raise ValidationError("Извините первая слова должно быть 'Hi' !")

# @deconstructible()
# class PhoneValidators():
#     def __call__(self, value):
#         v = re.match('^998(99|98|97|94|93)[0-9]{7}$', value)
#         if v and len(value) == 12:
#             return
#         raise ValidationError('Неверный номер, номер должно быть узбекским!')

# @deconstructible()
# class EmailValidators():
#     def __call__(self, *args, **kwargs):
