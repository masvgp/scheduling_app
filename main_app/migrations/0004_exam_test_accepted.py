# Generated by Django 3.0.4 on 2020-03-28 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_exam_test_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='test_accepted',
            field=models.BooleanField(default=False),
        ),
    ]