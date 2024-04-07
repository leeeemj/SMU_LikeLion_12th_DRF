from django.db import models
from users.models import User

# Create your models here.
class Recomment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='recomments',null=True)
    post = models.ForeignKey('posts.Post',on_delete=models.CASCADE,related_name='recomments',null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    uploaded_at=models.DateTimeField(auto_now=True)