from django.urls import path
from . import views




# Create your views here.
urlpatterns = [
    path('registration', views.register, name = 'register'),
]
