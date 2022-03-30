from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class CustomManager(BaseUserManager):
    def create_user(self, email, first_name, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault("is_active", True)
        other_fields.setdefault('is_superuser', True)


        if not email:
            raise ValueError("Provide an email address.")

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, **other_fields)

        # replace the "superuser" with what the default password should be as it is set
        # to make them change it when password is superuser
        ########

        user.set_password("superuser")

        ########

        user.save()

        return user

    def create_user(self, email, first_name, **other_fields):

        if not email:
            raise ValueError("Provide an email address.")

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, **other_fields)

        # replace the "testing" with what the default password should be as it is set
        # to make them change it when password is testing
        ########

        user.set_password("testing")

        ########

        user.save()

        return user

class Expertise():
    exp_name = models.TextField()
    exp_desc = models.TextField()

class Title():
    title_name = models.TextField()
    title_desc = models.TextField()

class Language():
    lang_name = models.TextField()

class Employee(AbstractBaseUser, PermissionsMixin):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    dob = models.CharField(max_length= 10)
    expertise = models.ManyToManyField('Expertise', null=True)
    title = models.ManyToManyField('Title')
    language = models.ManyToManyField('Language')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName', 'lastName', 'dob', 'title', 'language']

    def __str__(self):
        return self.first_name