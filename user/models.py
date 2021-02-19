from decimal import Decimal

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        validate_email(email)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('balance', 0)
        extra_fields.setdefault('phone_number', '0')
        extra_fields.setdefault('first_name', 'name')
        extra_fields.setdefault('last_name', 'last name')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    balance = models.DecimalField(
        max_digits=8, decimal_places=2,
        verbose_name=_('Balance'),
        default=Decimal(0)
    )
    phone_number = models.CharField(max_length=20, verbose_name=_('Phone Number'))
    first_name = models.CharField(max_length=20, verbose_name=_('First name'))
    last_name = models.CharField(max_length=20, verbose_name=_('Last name'))

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
