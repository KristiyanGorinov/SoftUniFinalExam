from django.core.validators import MinLengthValidator
from django.db import models
from users.validators import IsAlphaValidator

class User(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(3),
            IsAlphaValidator(),
        ]
    )

    last_name = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(3),
            IsAlphaValidator(),
        ]
    )
