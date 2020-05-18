from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django import forms

# Import Date Picker modules
from bootstrap_datepicker_plus import DatePickerInput

dates_to_disable = []


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
    comment = models.CharField(max_length=300, blank=True)
    test_accepted = models.BooleanField(default=False)

    def __str__(self):
        for i in Exam.objects.raw('Select * from main_app_exam where test_accepted == True'):
            AcceptedExams.objects.raw('INSERT INTO main_app_acceptedexams(instructor_first_name, instructor_last_name, department, course_name, course_number, section_number, num_students, calculator, notes, computer_exam, scantron, timed, dictionary, comment, test_accepted) VALUES (' + i.instructor_first_name + 
            ',' + i.instructor_last_name + ',' + i.department + ',' + i.course_name + ',' + i.course_number + ',' + 
            i.section_number + ',' + i.num_students + ',' + i.calculator + ',' + i.notes + ',' + i.computer_exam + ',' +
            i.scantron + ',' + i.timed + ',' + i.dictionary + ',' + i.comment + ',' + i.test_accepted + ')')
        return "{0}".format(
            self.course_name)


class AcceptedExams(models.Model):
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
    comment = models.CharField(max_length=300, blank=True)
    test_accepted = models.BooleanField(default=False)

class Date(models.Model):
    exam = models.OneToOneField(Exam,
                                on_delete=models.CASCADE,
                                primary_key=True,
                                default=True
                                )
    start_date = models.DateField()
    end_date = models.DateField()
    late_start_date = models.DateField(blank=True, null=True)
    late_end_date = models.DateField(blank=True, null=True)


class DisableDates(models.Model):
    date = models.DateField(default=0)
    num_students = models.IntegerField(null=True, default=0)
    disable_date = models.BooleanField(default=False)


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
            'comment'
        ]


class DateForm(ModelForm):
    def __init__(self, user_id = 1, *args, **kwargs): 
        super(DateForm, self).__init__(*args, **kwargs)
        self._id = user_id 

    def get_id(self):
        return self._id
    def set_id(self, x):
        self._id = x
    class Meta:
        model = Date

        fields = [
            'exam',
            'start_date',
            'end_date',
            'late_start_date',
            'late_end_date'
        ]
        exclude = ('exam',)
        widgets = {
            'start_date': DatePickerInput(
                options={
                    "disabledDates": dates_to_disable
                }).start_of('regular days'),
            'end_date': DatePickerInput().end_of('regular days'),
            'late_start_date': DatePickerInput().start_of('late days'),
            'late_end_date': DatePickerInput().end_of('late days'),
}
