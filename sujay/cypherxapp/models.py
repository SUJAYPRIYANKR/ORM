
from django.db import models
from django.contrib import admin
class blinkit(models.Model):
 name=models.CharField(max_length=10)
 Email=models.EmailField()
 cart=models.TextField()
 phone_no=models.IntegerField(primary_key=True)
 order_history=models.TextField()
 total_amtspent=models.IntegerField()
 alternative_phoneno=models.IntegerField()

class blinkitadmin(admin.ModelAdmin):
 list_details=["name","Email","cart","phone_no","order_history","total_amtspent","alternative_phoneno"]



