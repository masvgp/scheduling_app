# Generated by Django 3.0.4 on 2020-03-22 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20200320_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='test_accepted',
            field=models.BooleanField(default=False),
        ),
    ]