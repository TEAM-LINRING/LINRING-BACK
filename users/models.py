from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import EmailValidator
from .validators import EmailDomainValidate

from .managers import UserManager

# Create your models here.
class User(AbstractUser):
    email_validator = EmailDomainValidate()

    username = None
    email = models.EmailField(
        _('email address'),
        unique=True,
        # validators=[email_validator],
        validators=[EmailValidator(allowlist=["kookmin.ac.kr"])]
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email