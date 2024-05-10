from rest_framework.serializers import ModelSerializer
from . import models

class PostSerializers(ModelSerializer):
    
    class Meta:
        model = models.PO_MODEL
        fields = ('__all__')

