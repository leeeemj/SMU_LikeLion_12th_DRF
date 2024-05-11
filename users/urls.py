from django.urls import path

from users import views
#진짜 디자인할 패턴들, url나누는 기준은 view
urlpatterns = [
    #path('', views.user_list_api_view,name='user-list'),#users로 시작하는 모든 패턴은 users.urls가서 찾아라
    path('',views.user_join, name='user-join'),
    path('login/',views.user_login, name='user_login'),
    path('<int:pk>/', views.user_detail,name='user-detail'),
]
#전체조회는 list
#단일조회는 retrieve
 
