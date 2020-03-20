from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Exam, ExamForm
from .models import Date, DateForm
import datetime


# Create your views here.
def home(request):
    return HttpResponse('Home Page!')


def get_exam_info(request):
    '''View function gets exam info data from exam_info.html and pases it to ExamForm which passes the data to the Exam model which stores the data in the data base'''

    # The following block will slice the scheduled exams by a given date and then
    # count the number of students scheduled on that date. I should probably create
    # a database to store the total number of exam scheduled by day. This way, we can just
    # query this data base to set dates.
    # exam_query = Exam.objects.all()
    # exams_by_date = exam_query.filter(start_date=datetime.date(2020, 3, 31))
    # num_students_scheduled = 0
    # for exam in exams_by_date:
    #     num_students_scheduled += exam.num_students
    # print(num_students_scheduled)
    # print(Exam.objects.filter(start_date__lte='2020-03-31'))

    if request.method == 'POST':
        exam_form = ExamForm(request.POST)
        if exam_form.is_valid():
            exam_form.save()
            ''' Put function here that passes data from "exam_form" to confirmation page '''
            date_form = DateForm()
            return render(request, 'date_info.html', {'date_form': date_form})
    else:
        exam_form = ExamForm()

    return render(request, 'exam_info.html', {'exam_form': exam_form})


def get_date_info(request):
    if request.method == 'POST':
        date_form = DateForm(request.POST)
        if date_form.is_valid():
            date_form.save()

            return HttpResponseRedirect('/')

    else:
        date_form = DateForm()

    return render(request, 'date_info.html', {'date_form': date_form})

def test_request(request, id):
    exam_request = get_object_or_404(Exam, pk=id)
    return render(request, 'test_request.html', 
    {'exam_request': exam_request}
    )
