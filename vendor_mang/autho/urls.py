from django.urls import path
from .views import sign
from .views import login_view
from .views import logout_view


urlpatterns = [
    path('sign-up/', sign),
    path('login/', login_view),
    path('logout/', logout_view),

]
