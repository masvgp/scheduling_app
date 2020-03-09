from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Exam, ExamForm


# Create your views here.
def home(request):
    return HttpResponse('Home Page!')


def get_exam_info(request):
    '''View function gets exam info data from exam_info.html and pases it to ExamForm which passes the data to the Exam model which stores the data in the data base'''
    if request.method == 'POST':
        exam_form = ExamForm(request.POST)
        if exam_form.is_valid():
            exam_form.save()
            return HttpResponseRedirect('/')
    else:
        exam_form = ExamForm()

    return render(request, 'exam_info.html', {'exam_form': exam_form})


# def exam_info(request):
#     if request.method == "Post":
#         # test_request is for pulling user creds from the admin - use later after admin is set up
#         # test_request = Invitation(from_user=request.user)

#         form = exam_info_form(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('welcome')
#     else:
#         return render(request, "exam_info.html")
