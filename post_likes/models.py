from django.db import models
from users.models import User
# Create your models here.
class Post_like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_likes',null=True)
    post = models.ForeignKey('posts.Post',on_delete=models.CASCADE,related_name='post_likes',null=True)
    