# Generated by Django 4.0.3 on 2022-04-28 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expName', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileName', models.TextField(unique=True)),
                ('Url', models.URLField(default='Needs to add URL.', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lanName', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logDesc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleName', models.CharField(max_length=100, unique=True)),
                ('titleDesc', models.TextField(default='Ask a mananager to update this.')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DOB', models.CharField(max_length=10)),
                ('expertise', models.ManyToManyField(to='TrustApp.expertise')),
                ('files', models.ManyToManyField(to='TrustApp.files')),
                ('language', models.ManyToManyField(to='TrustApp.language')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='TrustApp.title')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
