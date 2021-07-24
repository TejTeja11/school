from django.contrib import admin
from finance.models import Teacher
class TeacherAdmin(admin.ModelAdmin):
    list_display=['id','empid','name','gender','exp','department','contact','gmail']

# Register your models here.
admin.site.register(Teacher)

# Register your models here.
