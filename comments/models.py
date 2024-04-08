from django.db import models
from users.models import User
from django.utils import timezone
# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments',null=True)
    post = models.ForeignKey('posts.Post',on_delete=models.CASCADE,related_name='comments',null=True)
    content=models.CharField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)