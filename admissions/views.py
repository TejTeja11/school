from django.shortcuts import render
from admissions.models import Student
from admissions.forms import StudentModelForm
from admissions.forms import StudentFeesModelForm
from admissions.forms import VendorForm
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.decorators import login_required
# Create your views here.
#function based views
@login_required
def homepage(request):
    return render(request,'index.html')
def logoutUser(request):
    return render(request,'logout.html')

@login_required
def addAdmissions(request):
    form=StudentModelForm
    studentform={'form':form}
    if request.method=='POST':
        form=StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
        return homepage(request)
    return render(request,'admissions/add_admissions.html',studentform)
@login_required
def admissionsReport(request):
    result=Student.objects.all()
    students={'allstudents':result}
    return render(request,'admissions/admissions_report.html',students)
def admissionsReportStudent(request):
    result=Student.objects.all()
    students={'allstudents':result}
    return render(request,'admissions/admissionstudent_report.html',students)

@login_required
def addVendor(request):
    form=VendorForm
    vform={'form':form}
    if request.method=='POST':
        form=VendorForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['address'])
            print(form.cleaned_data['contact'])
            print(form.cleaned_data['item'])
        return homepage(request)
    return render(request,'admissions/add-vendor.html',vform)

@login_required
def feecollectionreport(request):
    result=Student.objects.all()
    students={'allstudents':result}
    return render(request,'admissions/fee_collectionreport.html',students)

def feereport(request):
    result=Student.objects.all()
    students={'allstudents':result}
    return render(request,'admissions/fee_report.html',students)

@login_required
def studentresultupdate(request,id):
    s=Student.objects.get(id=id)
    form=StudentModelForm(instance=s)
    dict={'form':form}
    if request.method=='POST':
        form=StudentResultModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
        return studentresultreport(request)
    return render(request,'admissions/student_resultupdate.html',dict)

@login_required
def studentresultreport(request):
    result=Student.objects.all()
    students={'allstudents':result}
    return render(request,'admissions/student_resultreport.html',students)

def distudentresultreport(request):
    result=Student.objects.all()
    students={'allstudents':result}
    return render(request,'admissions/distudentresult_report.html',students)

@login_required
def deletestudent(request,id):
    s=Student.objects.get(id=id)
    s.delete()
    return admissionsReport(request)

@login_required
def updatestudent(request,id):
    s=Student.objects.get(id=id)
    form=StudentModelForm(instance=s)
    dict={'form':form}
    if request.method=='POST':
        form=StudentModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
        return admissionsReport(request)
    return render(request,'admissions/update_student.html',dict)
def feeupdate(request,id):
    s=Student.objects.get(id=id)
    form=StudentFeesModelForm(instance=s)
    dict={'form':form}
    if request.method=='POST':
        form=StudentFeesModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
        return feecollectionreport(request)
    return render(request,'admissions/update_studentfees.html',dict)

class FirstClassBasedView(View):
    def get(self,request):
        return HttpResponse("hii")
