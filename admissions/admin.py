from django.contrib import admin
from admissions.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','admno','name','gender','fathername','mothername','classname','contact','books_fees','bookfees_status','school_fees','schoolfees_status','bus_fees','busfees_status']


admin.site.register(Student,StudentAdmin)



# Register your models here.
