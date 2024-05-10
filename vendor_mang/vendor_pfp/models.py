from django.db import models
from uuid import uuid4


# Create your models here.

class Vendor_Profile(models.Model):

    name = models.CharField(max_length=100,null=True)
    contact_details = models.TextField(null=True)
    address = models.TextField(null=True)
    vendor_code = models.UUIDField(default=uuid4, unique=True)
    on_time_delivery_rate = models.FloatField(null=True)
    quality_rating_avg = models.FloatField(null=True)
    average_response_time = models.FloatField(null=True)
    fulfillment_rate = models.FloatField(null=True)