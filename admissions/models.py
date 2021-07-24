from django.db import models

# Create your models here.

class Student(models.Model):
    GENDER_CHOICES = (
        ("Boy", "Boy"),
        ("Girl", "Girl"),
    )
    admno = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length = 20,choices = GENDER_CHOICES,default = 'NONE')
    fathername = models.CharField(max_length=50,default="", editable=True)
    mothername = models.CharField(max_length=50,default="", editable=True)
    classname = models.PositiveIntegerField(default=1)
    contact=models.CharField(max_length=50)
    books_fees= models.PositiveIntegerField(default=0)
    bookfees_status = models.CharField(max_length=25,default="NONE", editable=True)
    school_fees= models.PositiveIntegerField(default=0)
    schoolfees_status = models.CharField(max_length=25,default="NONE", editable=True)
    bus_fees= models.PositiveIntegerField(default=0)
    busfees_status = models.CharField(max_length=25,default="NONE", editable=True)
