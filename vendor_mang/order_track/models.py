from django.db import models
from vendor_pfp.models import Vendor_Profile
from uuid import uuid4


# Create your models here.
class PO_MODEL(models.Model):
    
    po_number = models.UUIDField(default=uuid4, unique=True)
    vendor = models.ForeignKey(Vendor_Profile, on_delete=models.CASCADE,null=True)
    order_date = models.DateTimeField(auto_now=False, auto_now_add=True,null=True)  # Defaulting to the current date and time
    delivery_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=None,null=True)  # Defaulting to None
    items = models.JSONField(default=dict)
    quantity = models.IntegerField(default=0)
    status = models.CharField(max_length=50, default="pending")
    quality_rating = models.FloatField(null=True, default=None)
    issue_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=None)  # Defaulting to None
    acknowledgment_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, default=None)  # Allowing null values, defaulting to None

