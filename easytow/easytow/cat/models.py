import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Makes(models.Model):
    make = models.CharField(max_length=50)
    make_pic = models.FilePathField

class Cars(models.Model):
    question = models.ForeignKey(Makes, on_delete=models.CASCADE)
    car_pic = models.FilePathField

class Towbars(models.Model):
    something=models.ForeignKey(Cars, on_delete=models.CASCADE)
    part_number = models.CharField(max_length=50)
    fitted_price = models.DecimalField(max_digits=5, decimal_places=2)
    bar_price = models.DecimalField(max_digits=5, decimal_places=2)
    make = models.CharField(max_length=50)
    picture = models.FilePathField
    fitting_pdf = models.FilePathField
    pfj_url = models.URLField
    bumper_cuts = models.BooleanField
    visible_bumper_cuts = models.BooleanField
    electrics_coding = models.BooleanField
    bypass_required = models.BooleanField
    towing_weight = models.IntegerField
    nose_weight = models.IntegerField
    model_exclusions = models.CharField(max_length=200)
    last_updated = models.DateTimeField

class Customers(models.Model):
    title = models.CharField(max_length=10)# choices https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.DateField
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_number = models.BigIntegerField
    alt_number = models.BigIntegerField
    house_num = models.CharField(max_length=100)# Could also be house name/ unit number.
    postcode = models.CharField(max_length=10)
    email = models.EmailField
    ip_address = models.GenericIPAddressField

class Job(models.Model):
    something = models.ForeignKey(Customers, on_delete=models.CASCADE)
    #car Will point to car in cars table
    #bar Will point to bar in bars table
    booking_time = models.DateTimeField
    #payment_ref = models. Will link to online payment number
    fitting_time = models.DateTimeField
    price = models.DecimalField(max_digits=5, decimal_places=2)
    reg = models.CharField(max_length=10)
