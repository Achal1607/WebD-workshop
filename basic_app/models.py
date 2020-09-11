from django.db import models
from django.contrib.auth import get_user_model

Given_Choices=(("UnderGraduate","UnderGraduate"),("Graduate","Graduate"),("PhD","PhD"),("Academician","Academician"))
# Given_Choices1=(("YES","YES"),("NO","NO"))

class InstituteInfo(models.Model):
    User=get_user_model()
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    position=models.CharField(max_length=256,choices=Given_Choices)
    # isIITR=models.CharField(max_length=3,choices=Given_Choices1)
    institute=models.CharField(max_length=256)

class UserInfo(models.Model):
    User=get_user_model()
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    country_code=models.CharField(max_length=5,null=True,blank=True)
    ph_num=models.CharField(max_length=12,null=True,blank=True)
    pay_num=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.user.first_name
