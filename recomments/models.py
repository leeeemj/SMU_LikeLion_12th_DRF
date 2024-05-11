from django.db import models
from users.models import User

# Create your models here.
class Recomment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='recomments',null=True)
    post = models.ForeignKey('posts.Post',on_delete=models.CASCADE,related_name='recomments',null=True)
    comment = models.ForeignKey('comments.Comment',on_delete=models.CASCADE,related_name='recomments',null=True)
    content=models.CharField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    
class RecommentLike(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='recomment_likes',null=True)
    comment = models.ForeignKey('comments.Comment',on_delete=models.CASCADE,related_name='recomment_likes',null=True)
    