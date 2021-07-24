from django.urls import path

from admissions.views import addAdmissions
from admissions.views import admissionsReport
from admissions.views import addVendor
from admissions.views import feecollectionreport
from admissions.views import studentresultupdate
from admissions.views import studentresultreport
from admissions.views import deletestudent
from admissions.views import updatestudent
from admissions.views import FirstClassBasedView
from admissions.views import admissionsReportStudent
from admissions.views import feeupdate
from admissions.views import feereport
from admissions.views import distudentresultreport


urlpatterns = [
    path('newadm/',addAdmissions),
    path('admreport/',admissionsReport),
    path('newvendor/',addVendor),
    path('feecr/',feecollectionreport),
    path('feer/',feereport),
    path('updfee/<int:id>',feeupdate),
    path('str/<int:id>',studentresultupdate),
    path('strr/',studentresultreport),
    path('dstrr/',distudentresultreport),
    path('del/<int:id>',deletestudent),
    path('upd/<int:id>',updatestudent),
    path('admreports/',admissionsReportStudent),
    path('firstcls/',FirstClassBasedView.as_view()),
]
