from django.urls import path
from . import views


# Create your views here.
urlpatterns = [
    path('', views.post_index, name = 'post_index'),
]
