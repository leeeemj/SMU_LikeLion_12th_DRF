from django.db import models #ctrl 찍고 누르면 내용확인 가능
from django.contrib.auth.models import AbstractUser
# Create your models here.

#장고는 id 자동생성 
class User(AbstractUser):
    pass
   
