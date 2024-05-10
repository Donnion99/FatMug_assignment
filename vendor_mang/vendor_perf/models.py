from django.db import models
from vendor_pfp.models import Vendor_Profile

# Create your models here.

class Performance(models.Model):
    vendor= models.ForeignKey(Vendor_Profile, on_delete=models.CASCADE,null=True)
    date = models.DateField(null=True)
    on_time_delivery_rate= models.FloatField(null=True)
    quality_rating_avg= models.FloatField(null=True)
    average_response_time= models.FloatField(null=True)
    fulfillment_rate= models.FloatField(null=True)

