from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import PostSerializers
from .models import PO_MODEL
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Avg
from django.utils import timezone
from django.shortcuts import get_object_or_404
from order_track.models import PO_MODEL
from vendor_pfp.models import Vendor_Profile
# functions

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
def demo(request):
    a ={
        "Get" : "get/",
        "Create" : "create/",
        "Delete" : "put/",
        "Update": "update/",
        "single user": "get/<email>"
    }
    return Response(a)


@api_view(['GET','POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def orders(request):
    if request.method == 'GET':

        u = PO_MODEL.objects.all()
        serializer = PostSerializers(u, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        try:
            serializer = PostSerializers(data=request.data)

            if serializer.is_valid():
                serializer.save()

            return Response('Order Created')
        except Exception as e:
            return Response(f"Kindly add the Order with JSON data formatted correctly. {e}")

  

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def ack(request,po_id):
    try:
        calculate_average_response_time(po_id)
        serializer = PostSerializers(data=request.data)

        if serializer.is_valid():
                serializer.save()

        return Response('Order Created')
    except Exception as e:
        return Response(f"Kindly add the Order with JSON data formatted correctly. {e}")


@api_view(['GET','PUT','DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def order(request,po_id):
    if request.method == 'GET':
        try:

            user = PO_MODEL.objects.get(id = po_id)
            if user == None:
                return Response("Order not found")
            
            serializer = PostSerializers(user)
            return Response(serializer.data)
           
        except Exception :
            return Response("Order not found.")

    elif request.method == 'PUT':
        try:

            user = PO_MODEL.objects.get(id = po_id)
            if user == None:
                return Response("Order not found")
            
            serializer = PostSerializers(instance=user , data=request.data)

            if serializer.is_valid():
                serializer.save()

            return Response("Order Updated")
           
        except Exception :
            return Response("Order not found.")

    elif request.method == 'DELETE':
        try:

            user = PO_MODEL.objects.get(id = po_id)
        
            if user == None:
                return Response("Order not found")

            user.delete()

            return Response("Order deleted")
        
        except Exception :
                return Response("Order not found")



