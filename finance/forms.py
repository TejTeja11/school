from django import forms
from finance.models import Teacher
class TeacherModelForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields='__all__'
