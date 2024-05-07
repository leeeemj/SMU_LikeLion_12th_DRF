from django.urls import path
from recomment_likes import views

urlpatterns = [
    path('',views.recomment_like, name='recomment_like'),
]