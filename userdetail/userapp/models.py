from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class userdata(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)

    #additional fields

    img=models.ImageField(upload_to="userimg",blank=True)
    user_url=models.URLField(blank=True)

# RD rate of interest
class rd_amount(models.Model):
    total_amount=models.IntegerField()
    amount=models.IntegerField()
    noof_year=models.IntegerField()
    interst_amt=models.IntegerField()
    rate_of_interest=models.CharField(max_length=50)
    total_investement=models.BigIntegerField()
    total_returns=models.IntegerField()