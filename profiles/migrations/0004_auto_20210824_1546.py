# Generated by Django 3.2.6 on 2021-08-24 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20210823_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='default_first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='default_last_name',
        ),
    ]