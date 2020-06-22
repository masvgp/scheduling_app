from django.db import models
from django.forms import ModelForm
from django import forms
import uuid

# libraries to support sessions
import hashlib
import random
import sys
from . import constants


# Import Date Picker modules
from bootstrap_datepicker_plus import DatePickerInput

dates_to_disable = []


# This function creates a session hash to follow the user through the various stages of scheduling their exam
def create_session_hash():
    hash = hashlib.sha1()
    hash.update(str(random.randint(0, sys.maxsize)).encode('utf-8'))
    return hash.hexdigest()

# This model includes all database fields for the exam scheduling form


class Exam(models.Model):
    # Hash and Stage fields
    session_hash = models.CharField(max_length=40, unique=True)
    stage = models.CharField(max_length=10, default=constants.STAGE_1)

    # Exam info - Stage 1 fields
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

    # Date info - Stage 2 fields
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    late_start_date = models.DateField(blank=True, null=True)
    late_end_date = models.DateField(blank=True, null=True)

    hidden_fields = ['stage']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.session_hash:
            while True:
                session_hash = create_session_hash()
                if Exam.objects.filter(session_hash=session_hash).count() == 0:
                    self.session_hash = session_hash
                    break

    @staticmethod
    def get_fields_by_stage(stage):
        fields = ['stage']  # Must always be present
        if stage == constants.STAGE_1:
            fields.extend(['instructor_first_name', 'instructor_last_name', 'department', 'course_name', 'course_number', 'section_number', 'num_students', 'calculator', 'notes', 'computer_exam', 'scantron', 'timed', 'dictionary', 'comment'])
        elif stage == constants.STAGE_2:
            fields.extend(['start_date', 'end_date', 'late_start_date', 'late_end_date'])
        return fields


class ExamForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        hidden_fields = self.instance.hidden_fields
        for field in self.fields:
            if field in hidden_fields:
                self.fields.get(field).widget = forms.HiddenInput()


# class Date(models.Model):
#     exam = models.OneToOneField('Exam', primary_key=True, on_delete=models.CASCADE)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     late_start_date = models.DateField(blank=True, null=True)
#     late_end_date = models.DateField(blank=True, null=True)


class DisableDates(models.Model):
    date = models.DateField(default=0)
    num_students = models.IntegerField(null=True, default=0)
    disable_date = models.BooleanField(default=False)


# class ExamForm(ModelForm):
#     class Meta:
#         model = Exam
#         fields = [
#             'instructor_first_name',
#             'instructor_last_name',
#             'department',
#             'course_name',
#             'course_number',
#             'section_number',
#             'num_students',
#             'calculator',
#             'notes',
#             'computer_exam',
#             'scantron',
#             'timed',
#             'dictionary',
#             'comment'
#         ]


# class DateForm(ModelForm):

#     class Meta:
#         model = Date

#         fields = [
#             # 'exam',
#             'start_date',
#             'end_date',
#             'late_start_date',
#             'late_end_date'
#         ]
#         # exclude = ('exam',)
#         widgets = {
#             # 'exam': forms.HiddenInput,
#             'start_date': DatePickerInput(
#                 options={
#                     "disabledDates": dates_to_disable
#                 }).start_of('regular days'),
#             'end_date': DatePickerInput().end_of('regular days'),
#             'late_start_date': DatePickerInput().start_of('late days'),
#             'late_end_date': DatePickerInput().end_of('late days'),
#         }
