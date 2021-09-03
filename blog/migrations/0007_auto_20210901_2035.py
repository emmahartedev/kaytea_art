# Generated by Django 3.2.6 on 2021-09-01 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='user',
        ),
        migrations.AlterField(
            model_name='reply',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]