from django.db import models
from django.forms import ModelForm


# Create your models here.


class Exam(models.Model):
    instructor_first_name = models.CharField(max_length=30)
    instructor_last_name = models.CharField(max_length=30)
    department = models.CharField(max_length=30, null=True)
    course_name = models.CharField(max_length=30, null=True)
    course_number = models.IntegerField(null=True)
    section_number = models.IntegerField(null=True)
    num_students = models.IntegerField(null=True)
    calculator = models.CharField(max_length=30, blank=True)
    notes = models.CharField(max_length=30, blank=True)
    computer_exam = models.BooleanField(default=False)
    scantron = models.BooleanField(default=False)
    timed = models.BooleanField(default=False)
    dictionary = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    late_start_date = models.DateField(blank=True)
    late_end_date = models.DateField(blank=True)
    comment = models.CharField(max_length=300, blank=True)


class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = [
            'instructor_first_name',
            'instructor_last_name',
            'department',
            'course_name',
            'course_number',
            'section_number',
            'num_students',
            'calculator',
            'notes',
            'computer_exam',
            'scantron',
            'timed',
            'dictionary',
            'start_date',
            'end_date',
            'late_start_date',
            'late_end_date',
            'comment'
        ]
