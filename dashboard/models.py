from django.db import models

# Create your models here.

class QREvent(models.Model):
    title = models.CharField(max_length=10801)
    description = models.TextField()
    status = models.CharField(max_length=256)
    disabledesc = models.CharField(max_length=256)
    feeamount = models.CharField(max_length=50)
    enablepayment = models.CharField(max_length=50)

class QRForm(models.Model):
    eventid = models.CharField(max_length=64)
    fullname = models.CharField(max_length=512)
    noofmembers = models.CharField(max_length=64)
    gender = models.CharField(max_length=512)
    college = models.CharField(max_length=512)
    collegeaddress = models.CharField(max_length=512)
    address = models.CharField(max_length=512)
    contact = models.CharField(max_length=512)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=512)
    groupmembers= models.CharField(max_length=4000)