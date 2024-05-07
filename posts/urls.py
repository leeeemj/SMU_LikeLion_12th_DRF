from django.urls import path
from posts import views

urlpatterns = [
    path('',views.post_list, name='post-list'),
    path('<int:pk>/', views.post_detail,name='post-detail'),
    path('<int:pk>/comments/',views.post_comments,name='post-comments')
]