from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializers
from .models import Performance
from order_track.models import PO_MODEL
from vendor_pfp.models import Vendor_Profile
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Avg
from django.utils import timezone

def delivery_date(vendor_id):
    vendor = get_object_or_404(Vendor_Profile, id=vendor_id)
    completed = PO_MODEL.objects.filter(vendor=vendor, status="completed")
    before = completed.filter(acknowledgment_date__lte=F('delivery_date'))
    ratio = before.count() / completed.count()
    update = get_object_or_404(Vendor_Profile, id=vendor_id)
    update.on_time_delivery_rate = ratio
    update.save()
    return "Success"


def calculate_quality_rating_average(vendor_id):
    # Retrieve the vendor
    vendor = get_object_or_404(Vendor_Profile, id=vendor_id)
    
    # Filter completed POs of the vendor
    completed_pos = PO_MODEL.objects.filter(vendor=vendor, status="completed")
    
    # Filter completed POs with quality ratings
    completed_pos_with_ratings = completed_pos.exclude(quality_rating__isnull=True)
    
    # Calculate the average quality rating
    average_quality_rating = completed_pos_with_ratings.aggregate(Avg('quality_rating'))['quality_rating__avg']
    
    return average_quality_rating


def calculate_average_response_time(vendor_id):
    # Retrieve the vendor
    vendor = get_object_or_404(Vendor_Profile, id=vendor_id)
    
    # Filter acknowledged POs of the vendor
    acknowledged_pos = PO_MODEL.objects.filter(vendor=vendor, acknowledgment_date__isnull=False)
    
    # Calculate response times for acknowledged POs
    response_times = []
    for po in acknowledged_pos:
        response_time = po.acknowledgment_date - po.issue_date
        response_times.append(response_time.total_seconds() / 3600)  # Convert to hours
    
    # Calculate the average response time
    average_response_time = sum(response_times) / len(response_times) if response_times else 0
    
    return average_response_time

def calculate_fulfilment_rate(vendor_id):
    # Retrieve the vendor
    vendor = get_object_or_404(Vendor_Profile, id=vendor_id)
    
    # Count successfully fulfilled POs
    successfully_fulfilled_pos = PO_MODEL.objects.filter(vendor=vendor, status='completed', issues=None).count()
    
    # Count total issued POs
    total_issued_pos = PO_MODEL.objects.filter(vendor=vendor).count()
    
    # Calculate the fulfilment rate
    fulfilment_rate = (successfully_fulfilled_pos / total_issued_pos) * 100 if total_issued_pos != 0 else 0
    
    return fulfilment_rate






@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def vend_perf(request,vendor_id):
    try:
        # deliver = delivery_date(vendor_id)
        user = Performance.objects.get(id = vendor_id)
        if user == None:
            return Response("Vendor Profile not found")
        delivery_date(request,vendor_id)
        serializer = PostSerializers(user)
        return Response(serializer.data)

           
    except Exception :
        return Response("Vendor profile not found.")

    






    