from django.http import HttpResponse
from django.shortcuts import render
#from models import Exam


# Create your views here.
def home(request):
    return HttpResponse('Home Page!')


def exam_info(request):
    # Variables for display on the rendered page.
    # name = 'name'
    # number = 1234
    # context = {
    #     'name': name,
    #     'number': number
    # }

    return render(request, 'exam_info.html')


# class Exam:
#     def __init__(self, instructor_first_name, instructor_last_name,
#                  course_name,
#                  course_number,
#                  num_students,
#                  start_date,
#                  end_date,
#                  late_date_start,
#                  late_date_end,
#                  timed,
#                  notes,
#                  calculator,
#                  dictionary,
#                  comment):

#         self.instructor_first_name = instructor_first_name
#         self.instructor_last_name = instructor_last_name
#         self.course_name = course_name
#         self.course_number = course_number
#         self.num_students = num_students
#         self.start_date = start_date
#         self.end_date = end_date
#         self.late_date_start = late_date_start
#         self.late_date_end = late_date_end
#         self.timed = timed
#         self.notes = notes
#         self.calculator = calculator
#         self.dictionary = dictionary
#         self.comment = comment


# exams = [
#     Exam(
#         'Mike',
#         'Snyder',
#         'calculus',
#         1210,
#         30,
#         '2/20/20',
#         '2/21/20',
#         'none',
#         'none',
#         False,
#         False,
#         True,
#         True,
#         'This is an example.'
#     )
# ]

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
