from django.urls import path
from .views import *

urlpatterns = [
    path('',mainRepo),
    path('listStudent',listStudent),
    path('listStaff',listStaff)
]