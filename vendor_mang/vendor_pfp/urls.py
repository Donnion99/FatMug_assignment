from django.urls import path
from .views import user,Vendor

urlpatterns = [

    path('', user),
    path('<int:vendor_id>', Vendor),

]