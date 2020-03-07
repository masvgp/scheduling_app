# Generated by Django 3.0.4 on 2020-03-07 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200306_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam',
            old_name='late_date_end',
            new_name='late_end_date',
        ),
        migrations.RenameField(
            model_name='exam',
            old_name='late_date_start',
            new_name='late_start_date',
        ),
        migrations.AddField(
            model_name='exam',
            name='computer_exam',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='exam',
            name='department',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='scantron',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='exam',
            name='section_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='calculator',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='exam',
            name='course_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='course_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='dictionary',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='exam',
            name='instructor_first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='exam',
            name='instructor_last_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='exam',
            name='notes',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='exam',
            name='num_students',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='timed',
            field=models.BooleanField(default=False),
        ),
    ]
