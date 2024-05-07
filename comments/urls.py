from django.urls import path
from comments import views

urlpatterns = [
    path('',views.comment_create, name='comment-create'),
    path('<int:pk>/', views.comment_detail,name='comment-detail'),
    path('<int:pk>/recomments/', views.recomment_list,name='recomment-list')
]