from rest_framework.serializers import ModelSerializer
from . import models

class PostSerializers(ModelSerializer):
    
    class Meta:
        model = models.Performance
        fields = ('__all__')

