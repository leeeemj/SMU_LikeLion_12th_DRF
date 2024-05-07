from django.urls import path
from recomments import views

urlpatterns = [
    path('',views.recomment_create, name='comment-create'),
    path('<int:pk>/', views.recomment_detail,name='comment-detail'),
]