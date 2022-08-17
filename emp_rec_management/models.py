from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EmployeeDetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    emp_dept = models.CharField(max_length=100,null= True,blank=True)
    emp_desig = models.CharField(max_length=100,null= True,blank=True)
    contact_no = models.IntegerField(null= True,blank=True)
    start_date = models.DateTimeField(auto_now_add = True, null= True, blank=True)

    def __str__(self):
        return self.user.username

