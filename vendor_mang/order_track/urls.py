from django.urls import path
from .views import orders,order,ack

urlpatterns = [

    path('', orders),
    path('<int:po_id>', order),
    path('<int:po_id>/acknowledge', ack),

]