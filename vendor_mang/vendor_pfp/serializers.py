from rest_framework.serializers import ModelSerializer
from . import models

class PostSerializers(ModelSerializer):
    
    class Meta:
        model = models.Vendor_Profile
        fields = ('__all__')

