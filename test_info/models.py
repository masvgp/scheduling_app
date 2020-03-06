from django.db import models

# Create your models here.


class exam_info(models.Model):
    instructor_first_name = models.CharField(max_length=30, blank=True)
    instructor_last_name = models.CharField(max_length=30, blank=True)
    course_name = models.CharField(max_length=30, blank=True)
    course_number = models.IntegerField(blank=True)
    num_students = models.IntegerField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    late_date_start = models.DateField()
    late_date_end = models.DateField()
    timed = models.BooleanField()
    notes = models.BooleanField()
    calculator = models.BooleanField()
    dictionary = models.BooleanField()
    comment = models.CharField(max_length=300, blank=True)
