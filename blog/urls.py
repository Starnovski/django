from django.urls import path
from . import views


# Create your views here.
urlpatterns = [
    path('', views.post_index, name = 'post_index'),
    path('post/<int:pk>', views.post_show, name = 'post_show'),
    path('post/<int:pk>/new_comment', views.comment_new, name = 'comment_new'),
]
