from django.db import models
from django.contrib.auth.models import User

class Language(models.Model):
    lanName = models.CharField(max_length=100)


class Expertise(models.Model):
    expName = models.CharField(max_length=100)
    expDesc = models.TextField


class Title(models.Model):
    titleName = models.CharField(max_length=100)
    titleDesc = models.TextField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT )
    firstName = models.TextField
    lastName = models.TextField
    DOB = models.CharField(max_length=10)
    expertise = models.ManyToManyField('Expertise')
    title = models.ForeignKey(Title, on_delete=models.PROTECT)
    language = models.ManyToManyField('Language')
