from django.db import models
from users.models import User

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments',null=True)
    post = models.ForeignKey('posts.Post',on_delete=models.CASCADE,related_name='comments',null=True)
    content=models.CharField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True)
    updated_at=models.DateTimeField(auto_now=True, null=True)

class CommentLike(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment_likes',null=True)
    comment = models.ForeignKey('comments.Comment',on_delete=models.CASCADE,related_name='comment_likes',null=True)
    