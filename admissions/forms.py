from django import forms
from admissions.models import Student

class StudentModelForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','admno','gender','fathername','mothername','classname','contact']
class VendorForm(forms.Form):
    name=forms.CharField()
    address=forms.CharField()
    contact=forms.CharField()
    item=forms.CharField()

class StudentFeesModelForm(forms.ModelForm):
    class Meta:
        model=Student
        fields = ['books_fees','bookfees_status','school_fees','schoolfees_status','bus_fees','busfees_status']
