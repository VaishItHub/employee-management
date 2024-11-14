from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    employee_name=models.CharField(max_length=255)
    employee_address=models.TextField()
    employee_phone_number=models.CharField( max_length=15)
    employee_email=models.EmailField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
