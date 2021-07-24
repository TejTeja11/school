from django.urls import path
from finance.views import addstaff
from finance.views import staffreport
from finance.views import salary
from finance.views import salaryreport
from finance.views import deletestaff
from finance.views import updatestaff
from finance.views import disstaffreport
from finance.views import feepayment

urlpatterns = [
    path('fee/',addstaff),
    path('duesreport/',staffreport),
    path('distaffrepo/',disstaffreport),
    path('sry/',salary),
    path('sryr/',salaryreport),
    path('delst/<int:id>',deletestaff),
    path('updst/<int:id>',updatestaff),
    path('payf/',feepayment),
]
