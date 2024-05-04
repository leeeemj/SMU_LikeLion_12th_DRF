from django.urls import path
from posts import views

urlpatterns = [
    path('',views.post_list, name='post-list'),
    path('<int:pk>/', views.post_detail,name='post-detail')
    ##url 작성 규칙에 앱이름 써야된다고 써있었는데 
    ##conpig urls.py에서 적었으니까 안 적어도 되는건가요 ?
]