from django.urls import path
from opensource import views

urlpatterns = [
   
    path('home/',views.home),
    path('student/<st_id>',views.getStudent),
    path('all/',views.getAllStudents)
]