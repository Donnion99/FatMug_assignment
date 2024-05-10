from django.urls import path
from .views import vend_perf

urlpatterns = [

    path('performance', vend_perf),

]