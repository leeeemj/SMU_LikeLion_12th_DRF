from django.urls import path
from recomments import views

urlpatterns = [
    path('<int:comment_id>',views.recomment_create, name='comment-create'),
    path('comment/<int:pk>/', views.recomment_detail,name='comment-detail'),
    path('<int:pk>/recommentlike/',views.recomment_like, name='recomment_like'),
]