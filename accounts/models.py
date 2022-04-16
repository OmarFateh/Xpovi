from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.password_validation import validate_password


class UserManager(BaseUserManager):
    """Custom user model manager."""
    def validate_email_address(self, email):
        """Take email and check if it's a valid email."""
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_('You must provide a valid email address.'))
            
    def validate_password(self, password):
        """Take password and check if it's a valid password."""
        try:
            validate_password(password)
        except ValidationError as e:
            raise ValueError(e)

    def create_user(self, username, email, password, **extra_fields):
        """Create and save a User with the given username, email and password."""
        if not username:
            raise ValueError(_('Users must have a username'))
        if email:
            # Normalize the email address by lowercasing the domain part of it.
            email = self.normalize_email(email)
            self.validate_email_address(email)
        else:    
            raise ValueError(_('Users must have an email address'))
        if password:
            self.validate_password(password)
        else:
            raise ValueError(_('Users must have a password'))
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        """Take username, email and password, and create superuser."""
        user = self.create_user(username, email, password=password, is_staff=True, is_superuser=True)    
        return user


class User(AbstractUser):
    """Custom user model, where email is unique."""
    email = models.EmailField(max_length=150, unique=True, verbose_name=_("Email"),
        error_messages={'unique': _('A user with that email already exists.')},
        validators=[validate_email])
    is_verified = models.BooleanField(default=False, verbose_name=_("Is Verified"))
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_("Timestamp"))

    def __str__(self):
        return self.username