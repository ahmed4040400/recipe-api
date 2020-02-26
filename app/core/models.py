from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# tha manager that handles adding user objects to the user model
class UserManager(BaseUserManager):
    # create a normal user
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("the user must has an email")
        # the **extra_field field is if i ever wanted to add
        # some extra information to the user
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # create a user with admin permissions
    def create_superuser(self, email, password):
        user = self.create_user(email=email,password=password)
        user.is_staff = True
        user.is_superuser = True
        return user


# creating the Custom user model
class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    # has admin permissions
    is_staff = models.BooleanField(default=False)
    # the manager
    objects = UserManager()
    # replacing the username field with the email field
    USERNAME_FIELD = 'email'
    # some required fields
    REQUIRED_FIELDS = ['name', ]
