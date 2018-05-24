from django.urls import path
from apiv1 import views

urlpatterns = [
    path('user-icon/<str:screen_name>/', views.user_icon, name='user_icon'),
]
