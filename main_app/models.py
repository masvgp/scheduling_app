from django.db import models
from django.forms import ModelForm

# Import Date Picker modules
from bootstrap_datepicker_plus import DatePickerInput


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


class Date(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    late_start_date = models.DateField(blank=True, null=True)
    late_end_date = models.DateField(blank=True, null=True)


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
    class Meta:
        model = Date
        fields = [
            'start_date',
            'end_date',
            'late_start_date',
            'late_end_date'
        ]
        widgets = {
            'start_date': DatePickerInput(
                options={
                    "disabledDates": ['03/10/2020', '03/11/2020']
                }).start_of('regular days'),
            'end_date': DatePickerInput().end_of('regular days'),
            'late_start_date': DatePickerInput().start_of('late days'),
            'late_end_date': DatePickerInput().end_of('late days'),
        }

    '''
    The following __init__ and functions are used to create a
    list of dates to be blocked out in the ExamForm
    '''

    # def __init__(self):
    #     self.start_date = start_date
    #     self.end_date = end_date

    # def date_range_list(self, start_date, end_date):
    # '''
    # Create a list of dates for a given date range.
    # '''
    #     date_range_length = (self.end_date - self.start_date).days
    #     date_list = [self.start_date, ]
    #     for day in range(1, date_range_length + 1):
    #         date_list.append(self.start_date + datetime.timedelta(day))

    #     return date_list
