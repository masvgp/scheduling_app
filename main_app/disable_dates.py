'''
This script contains various functions for handling user start_date and end_date input. The functions will create a list of dates between start_date and end_date. These dates will be checked against the DisableDates database. If student populations are beyond the threshold for the given dates, then those dates will be appended to the dates_to_disable variable.
'''
# Import models
from .models import Exam, DisableDates
# Import modules
from datetime import datetime, timedelta
# from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseRedirect

#print(datetime.strptime('03/23/2020', '%m/%d/%Y').date())


def date_range_list(request_post_copy):
    '''
    Create a list of dates for a given date range.
    '''
    start_date = datetime.strptime(request_post_copy.get('start_date'), '%m/%d/%Y').date()
    end_date = datetime.strptime(request_post_copy.get('end_date'), '%m/%d/%Y').date()

    date_range_length = (end_date - start_date).days
    date_list = [start_date, ]

    for day in range(1, date_range_length + 1):
        date_list.append(start_date + timedelta(day))

    return date_list


# date_range_list test
# print(date_range_list(datetime.date(2020, 3, 31), datetime.date(2020, 4, 5)))


def update_disabled_dates_db(day, request_post_copy):
    '''
    Function takes an argument 'date' adds the number of students schedule to the 'disabled_dates' database
    '''
    threshold = 100
    disabled_dates_db = DisableDates.objects.all()
    exam_db = Exam.objects.all()
    current_user_record = request_post_copy
    current_user_num_students = exam_db.get(id=current_user_record.get('Exam_id')).num_students  # Currently this is wrong... the id is unfortunately not passed on to the subsequent 'child' forms from the 'parent' until database changes are commited, which doesn't happen till after a post request.
    prior_num_students_on_date = disable_dates_db.get(date=day).num_students

    if disable_dates_db.filter(date=day):
        total_num_students_on_date = prior_num_students_on_date + current_user_num_students

        if total_num_students_on_date < threshold:
            disable_dates_db.filter(date=day).update(num_students=total_num_students_on_date)
        else:
            disable_dates_db.filter(date=day).update(num_students=total_num_students_on_date, disable_date=True)

    elif current_user_num_students < threshold:
        DisableDates.objects.create(date=day, num_students=current_user_num_students, disable_date=False)
    else:
        DisableDates.objects.create(date=day, num_students=current_user_num_students, disable_date=True)

    # exam_db = Exam.objects.all()
    # exams_on_date = exam_query.filter(start_date=date)
    # num_students_scheduled = 0
    # for exam in exams_by_date:
    #     num_students_scheduled += exam.num_students
    # print(num_students_scheduled)
    # print(Exam.objects.filter(start_date__lte='2020-03-31'))
