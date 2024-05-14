from django.urls import path
from recomments import views

urlpatterns = [
    path('<int:comment_id>/',views.recomment_create, name='recomment-create'),
    path('comment/<int:pk>/', views.recomment_detail,name='recomment-detail'),
    path('<int:recomment_id>/recommentlike/',views.recomment_like, name='rerecomment_like'),
]