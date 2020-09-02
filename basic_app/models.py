from django.db import models
from django.contrib.auth import get_user_model

class UserInfo(models.Model):
    User=get_user_model()
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    country_code=models.CharField(max_length=5,null=True,blank=True)
    ph_num=models.CharField(max_length=12,null=True,blank=True)
    pay_num=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.user.first_name
