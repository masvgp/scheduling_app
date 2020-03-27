from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Exam, ExamForm, Date, DateForm, DisableDates, dates_to_disable
from datetime import datetime, timedelta
from main_app.disable_dates import date_range_list, update_disabled_dates_db
from .models import Exam, ExamForm
from .models import Date, DateForm
import datetime



# Create your views here.


def home(request):
    return HttpResponse('Home Page!')


def get_exam_info(request):
    '''
    View function gets exam info data from exam_info.html and pases it to ExamForm which passes the data to the Exam model which stores the data in the data base
    '''
    exam_db = Exam.objects.all()
    # print(exam_db.get(num_students=30).num_students)
    #print(exam_db.filter(num_students=30).update(num_students=exam_db.get(num_students=30) + 10))
    # print(Exam.objects.get(pk=2))
    # if 'num_students' in request.GET:
    #     print(request.GET['num_students'])

    if request.method == 'POST':
        exam_instance = Exam()
        exam_form = ExamForm(request.POST, instance=exam_instance)
        if exam_form.is_valid():
            exam_form.save()
            print(exam_instance)

            ''' Put function here that passes data from "exam_form" to confirmation page '''
            date_form = DateForm()
            return render(request, 'date_info.html', {'date_form': date_form})
    else:
        exam_form = ExamForm()

    return render(request, 'exam_info.html', {'exam_form': exam_form})


def get_date_info(request, id):
    get_id = get_object_or_404(Exam, pk=id)
    print(get_id)
    # dates_to_disable.append('03/31/2020')
    # print(dates_to_disable)
    if request.method == 'POST':
        date_instance = Date()
        date_form = DateForm(request.POST, instance=date_instance)

        if date_form.is_valid():
            # cleaned_form = date_form.cleaned_data
            # print(cleaned_form)
            date_form.save()
            print(date_instance)

            # The following outputs the list of days from start date to end date given by the user
            # request_post_copy = request.POST.copy()
            # current_user_dates = date_range_list(request_post_copy)

            # The following loops through the date list and updates the DisableDates database according to the number of students scheduled.
            # for day in current_user_dates:
            #     update_disabled_dates_db(day, request_post_copy)
            # print(request_post_copy)

            return HttpResponseRedirect('/')

    else:
        date_form = DateForm()

    return render(request, 'date_info.html', {'date_form': date_form})

def test_request(request):
    exam_request = Exam.objects.get(id=1)
    if request.POST.get("Accept"):
        Exam.test_accepted = True
        return render(request, '/')
    elif request.POST.get("Decline"):
        return render(request, 'test_request.html', 
                    {'exam_request': exam_request}
                    )    
    return render(request, 'test_request.html', 
                {'exam_request': exam_request}
                )
