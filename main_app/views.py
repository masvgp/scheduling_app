from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Exam, ExamForm
# from .models import Date, DateForm, DisableDates, dates_to_disable # Currently not needed
from datetime import datetime, timedelta
from main_app.disable_dates import date_range_list, update_disabled_dates_db
from django.db import connection
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.views import View

# libraries to support the sessions version
from django.forms import modelform_factory
from django.urls import reverse
from . import constants


# This function accesses the exam form by hash value.


def get_exam_from_hash(session_hash):
    # Find and return a not-yet-completed Exam with a matching session_hash, or None if no such object exists.
    return Exam.objects.filter(session_hash=session_hash, ).exclude(stage=constants.COMPLETE).first()

# Homepage View


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)

# Exam form view


class ExamView(FormView):
    template_name = 'exam_info.html'
    exam = None
    form_class = None

    def dispatch(self, request, *args, **kwargs):
        session_hash = request.session.get("session_hash", None)
        # Get the exam for this session. It could be None.
        self.exam = get_exam_from_hash(session_hash)
        # Attach the request to 'self' so 'form_valid()' can access it below.
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # This data is valid, so set this form's session hash in the session.
        self.request.session['session_hash'] = form.instance.session_hash
        current_stage = form.cleaned_data.get('stage')
        # Get the next stage after this one.
        new_stage = constants.STAGE_ORDER[constants.STAGE_ORDER.index(current_stage) + 1]
        form.instance.stage = new_stage
        form.save()  # This will save the underlying instance.
        if new_stage == constants.COMPLETE:
            return redirect(reverse('main_app:home'))
        # else
        return redirect(reverse('main_app:exam_info'))

    def get_form_class(self):
        # If we found an exam that matches the session hash, look at its 'stage' attribute to decide which stage of the application we're on. Otherwise, assume we're on stage 1.
        stage = self.exam.stage if self.exam else constants.STAGE_1
        # Get the form fields appropriate to that stage.
        fields = Exam.get_fields_by_stage(stage)
        # Use those fields to dynamically create a form with "modelform_factory"
        return modelform_factory(Exam, ExamForm, fields)

    def get_form_kwargs(self):
        # Make sure Django uses the same Exam instance we've already been working on.
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.exam
        return kwargs


# Create your views here.


# def home(request):
#     return HttpResponse('Home Page!')

# class HomePageView(TemplateView):
#     template_name = 'home.html'

#     def get(self, request):
#         return render(request, self.template_name)


# class ExamView(View):
#     template_name = 'exam_info.html'
#     form_class = ExamForm
#     exam_instance = Exam()

#     def get(self, request):
#         exam_form = self.form_class(instance=self.exam_instance)

#         return render(request, self.template_name, {'exam_form': exam_form})

#     def post(self, request):
#         exam_form = self.form_class(request.POST, instance=self.exam_instance)
#         if exam_form.is_valid():
#             exam_form.save()
#         # print(self.exam_instance)
#         return HttpResponse('date_info.html')

#         # return render(request, self.template_name, {'exam_form': exam_form})
#         return render(request, 'date_info.html', {'date_form': DateForm()})


# class DateView(ExamView, View):
#     template_name = 'date_info.html'
#     form_class = DateForm

#     def get(self, request):

#         date_form = self.form_class()
#         return render(request, self.template_name, {'date_form': date_form})

#     def post(self, request):
#         print(self.exam_instance.id)
#         date_form = self.form_class()
#         if date_form.is_valid():
#             date_form.save()
#         return render(request, 'home.html')


# def get_exam_info(request):

#     exam_db = Exam.objects.all()

#     if request.method == 'POST':
#         exam_instance = Exam()
#         exam_form = ExamForm(request.POST, instance=exam_instance)
#         if exam_form.is_valid():
#             exam_form.save()

#             # print(exam_instance)

#             date_form = DateForm()
#             return render(request,
#                           'date_info.html',
#                           {'date_form': date_form,
#                            'exam_instance': exam_instance}
#                           )
#     else:
#         exam_form = ExamForm()

#     return render(request, 'exam_info.html', {'exam_form': exam_form})


# def get_date_info(request):

#     form = DateForm(request.POST or None)
#     if form.is_valid():
#         # print(form)
#         # current_date_obj = Date.objects.create(**form.cleaned_data)
#         # print(current_date_obj)
#         # current_date_obj.save()
#         return HttpResponseRedirect('/')

#     context = {
#         'form': form
#     }

#     return render(request, 'date_info.html', context)

    # if request.method == 'POST':
    #     #date_instance = Date()
    #     # print(date_instance)
    #     date_form = DateForm(request.POST)
    #     if date_form.is_valid():
    #         # print(request.POST)
    #         date_form.save()
    #         # print(date_instance)

    #         # current_user_id = date_instance.exam_ptr_id
    #         # print(current_user_id)

    #         return HttpResponseRedirect('/')

    # else:
    #     date_form = DateForm()

    #     user_id = exam_instance.id

    # return render(request,
    #               'date_info.html',
    #               {'date_form': date_form,
    #                'exam_instance': exam_instance})

    # print(exam_db.get(num_students=30).num_students)
    #print(exam_db.filter(num_students=30).update(num_students=exam_db.get(num_students=30) + 10))
    # print(Exam.objects.get(pk=2))
    # if 'num_students' in request.GET:
    #     print(request.GET['num_students'])

    # print(date_instance.exam_ptr_id)
    # The following outputs the list of days from start date to end date given by the user
    # request_post_copy = request.POST.copy()
    # current_user_dates = date_range_list(request_post_copy)

    # The following loops through the date list and updates the DisableDates database according to the number of students scheduled.
    # for day in current_user_dates:
    #     update_disabled_dates_db(day, request_post_copy)
    # print(request_post_copy)
