from django.urls import path
from comment_likes import views

urlpatterns = [
    path('',views.comment_like, name='commentlike-detail'),
]