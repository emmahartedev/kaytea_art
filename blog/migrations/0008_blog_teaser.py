# Generated by Django 3.2.6 on 2021-09-07 09:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210901_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='teaser',
            field=models.TextField(default=' test  test  test  test  test  test  test  test  test  test  test  test  test  test  test  test  test  test  test  test ', validators=[django.core.validators.MinLengthValidator(70)]),
            preserve_default=False,
        ),
    ]
