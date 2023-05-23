from django.urls import path
from .views import *

urlpatterns = [
    path('',list),
    path('add/',insert),
    path('edit/<int:id>',update),
    path('delete/<int:id>',delete)
]
