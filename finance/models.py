from django.db import models

# Create your models here.
class Teacher(models.Model):
    GENDER_CHOICES = (
        ("Male", "M"),
        ("Female", "F"),
    )
    empid = models.PositiveIntegerField(default=0,unique=True)
    name=models.CharField(max_length=50)
    gender = models.CharField(max_length = 20,choices = GENDER_CHOICES,default = 'NONE')
    exp=models.CharField(max_length=25,default="", editable=True)
    department=models.CharField(max_length=50)
    contact=models.CharField(max_length=100)
    gmail=models.CharField(max_length=30)
