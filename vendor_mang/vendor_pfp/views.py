from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializers
from .models import Vendor_Profile
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



@api_view(['GET','POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def user(request):
    if request.method == 'GET':

        u = Vendor_Profile.objects.all()
        serializer = PostSerializers(u, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        try:
            serializer = PostSerializers(data=request.data)

            if serializer.is_valid():
                serializer.save()

            return Response('Vendor Added')
        except Exception as e:
            return Response(f"Kindly add the vendor with JSON data formatted correctly. {e}")

  


@api_view(['GET','PUT','DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def Vendor(request,vendor_id):
    if request.method == 'GET':
        try:

            user = Vendor_Profile.objects.get(id = vendor_id)
            if user == None:
                return Response("Vendor Profile not found")
            
            serializer = PostSerializers(user)
            return Response(serializer.data)
           
        except Exception :
            return Response("Vendor profile not found.")

    elif request.method == 'PUT':
        try:

            user = Vendor_Profile.objects.get(id = vendor_id)
            if user == None:
                return Response("Vendor Profile not found")
            
            serializer = PostSerializers(instance=user , data=request.data)

            if serializer.is_valid():
                serializer.save()

            return Response("Vendor Profile Updated")
           
        except Exception :
            return Response("Vendor profile not found.")

    elif request.method == 'DELETE':
        try:

            user = Vendor_Profile.objects.get(id = vendor_id)
        
            if user == None:
                return Response("Vendor Profile not found")

            user.delete()

            return Response("Vendor Profile deleted")
        
        except Exception :
            return Response("Vendor profile not found.")



