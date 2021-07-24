from django.shortcuts import render
from django.shortcuts import render
from finance.models import Teacher
from finance.forms import TeacherModelForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def homepage(request):
    return render(request,'index.html')
@login_required
def addstaff(request):
    form=TeacherModelForm
    staffform={'form':form}
    if request.method=='POST':
        form=TeacherModelForm(request.POST)
        if form.is_valid():
            form.save()
        return homepage(request)
    return render(request,'finance/add_staff.html',staffform)
@login_required
def staffreport(request):
    result=Teacher.objects.all()
    staffs={'allstudents':result}
    return render(request,'finance/staff_report.html',staffs)
@login_required
def salary(request):
    return render(request,'finance/salary.html')
@login_required
def salaryreport(request):
    return render(request,'finance/salary_report.html')
@login_required
def deletestaff(request,id):
    s=Teacher.objects.get(id=id)
    s.delete()
    return staffreport(request)
@login_required
def updatestaff(request,id):
    s=Teacher.objects.get(id=id)
    form=TeacherModelForm(instance=s)
    dict={'form':form}
    if request.method=='POST':
        form=TeacherModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
        return staffreport(request)
    return render(request,'finance/update_staff.html',dict)
def disstaffreport(request):
    result=Teacher.objects.all()
    staffs={'allstudents':result}
    return render(request,'finance/disstaff_report.html',staffs)
def feepayment(request):
    return render(request,'finance/payment.html')

# Create your views here.
