from django.urls import path
from . import views

urlpatterns = [
    path('auth/',views.user_list_create, name='user_list_create'),
]
