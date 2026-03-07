from django.urls import path
from . import views

urlpatterns = [
    path('category/',views.category_list_create, name='category_list_create'),
     path('course/',views.course_list_create, name='course_list_create'),
]
