from tkinter import N
from django.db import models
from django.contrib.auth.models import User

class Language(models.Model):
    lanName = models.CharField(max_length=100)

    def __str__(self):
        return self.lanName


class Expertise(models.Model):
    expName = models.CharField(max_length=100)

    def __str__(self):
        return self.expName


class Files(models.Model):
    fileName = models.TextField(null=False)

class Log(models.Model):
    logDesc = models.TextField(null=False)


class Title(models.Model):
    titleName = models.CharField(max_length=100)
    titleDesc = models.TextField(null=False, default='Ask a mananager to update this.')

    def __str__(self):
        return self.titleName

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT )
    DOB = models.CharField(max_length=10)
    expertise = models.ManyToManyField('Expertise')
    title = models.ForeignKey(Title, on_delete=models.PROTECT)
    language = models.ManyToManyField('Language')
    files = models.ManyToManyField('Files')

    def __str__(self):
        return self.user.username
