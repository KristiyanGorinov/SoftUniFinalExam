from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError

@deconstructible
class IsAlphaValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Your name must contain letters only!"
        else:
            self.__message = value


    def __call__(self, value:str, *args, **kwargs):
        if not value.isalpha():
            raise ValidationError(self.message)
