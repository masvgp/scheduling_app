from django.forms import ModelForm

from .models import exam_info


class exam_info_form(ModelForm):
    class Meta:
        model = exam_info
