from django.urls import path
from posts import views

urlpatterns = [
    path('',views.post_list, name='post-list'),
    #프론트에서 url로 넣어주는 거
    path('<int:post_id>/', views.post_detail,name='post-detail'),
    path('<int:post_id>/comments/',views.post_comments,name='post-comments'),
    path('<int:post_id>/postlikes/',views.post_like, name='post_like')
]