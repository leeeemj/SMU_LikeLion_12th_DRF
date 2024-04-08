from django.db import models
from users.models import User
from django.utils import timezone

# Create your models here.
class Recomment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='recomments',null=True)
    post = models.ForeignKey('posts.Post',on_delete=models.CASCADE,related_name='recomments',null=True)
    comment = models.ForeignKey('comments.Comment',on_delete=models.CASCADE,related_name='recomments',null=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)