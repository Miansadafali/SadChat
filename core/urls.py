from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('request_friendship/<int:recipient_id>/', views.request_friendship, name='request_friendship'),
]
