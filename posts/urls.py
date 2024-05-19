from django.urls import path
from posts import views


urlpatterns = [
    #FBV urls
    #path('',views.post_list, name='post-list'),
    #path('<int:post_id>/', views.post_detail,name='post-detail'),
    path('<int:post_id>/comments/',views.post_comments,name='post-comments'),
    path('<int:post_id>/postlikes/',views.post_like, name='post_like'),
    
    #generics 
    path('',views.PostListView.as_view(),name='post_list'),
    path('<int:pk>/',views.PostDetailView.as_view),
    # path('<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    

    
]
