from django.contrib import admin
from main_app.models import Exam, Date, AcceptedExams

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'num_students', 'instructor_last_name', 'test_accepted')
    list_editable = ('test_accepted',)

@admin.register(AcceptedExams)
class AcceptedExamsAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'num_students', 'instructor_last_name', 'test_accepted')
    list_editable = ('test_accepted',)

admin.site.register(Date)

