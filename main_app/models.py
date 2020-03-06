from django.db import models

# Create your models here.


class Exam(models.Model):
    instructor_first_name = models.CharField(max_length=30, blank=True)
    instructor_last_name = models.CharField(max_length=30, blank=True)
    department = models.CharField(max_length=30, blank=True)
    course_name = models.CharField(max_length=30, blank=True)
    course_number = models.IntegerField(blank=True)
    section_number = models.IntegerField(blank=True)
    num_students = models.IntegerField(blank=True)
    calculator = models.CharField(max_length=30, blank=True)
    notes = models.CharField(max_length=30, blank=True)
    computer_exam = models.BooleanField()
    scantron = models.BooleanField()
    timed = models.BooleanField()
    dictionary = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField()
    late_start_date = models.DateField()
    late_end_date = models.DateField()
    comment = models.CharField(max_length=300, blank=True)
