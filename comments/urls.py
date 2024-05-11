from django.urls import path
from comments import views

urlpatterns = [
    path('<int:post_id>/',views.comment_create, name='comment-create'),
    path('post/<int:comment_id>/', views.comment_detail,name='comment-detail'), 
    path('<int:comment_id>/recomments/', views.recomment_list,name='recomment-list'),
    path('<int:comment_id>/commentlikes/',views.comment_like, name='comment_like'),
]