# Generated by Django 3.2.6 on 2021-09-16 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_productreview_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length='200', null=True),
        ),
    ]
