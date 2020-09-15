from django.db import models
from django.contrib.auth import get_user_model

Given_Choices=(("UnderGraduate","UnderGraduate"),("Graduate","Graduate"),("PhD","PhD"),("Academician","Academician"))
Given_Choices1=(("YES","YES"),("NO","NO"))

class UserInfo(models.Model):
    User=get_user_model()
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    ph_num=models.CharField(max_length=20,null=True,blank=True)
    position=models.CharField(max_length=256,choices=Given_Choices,default="UnderGraduate")
    isIITR=models.CharField(max_length=3,choices=Given_Choices1,default="YES",blank=True,null=True)
    institute=models.CharField(max_length=256,blank=True,null=True)
    pay_num=models.CharField(max_length=50,null=True,blank=True)
    
    def __str__(self):
        return self.user.first_name
