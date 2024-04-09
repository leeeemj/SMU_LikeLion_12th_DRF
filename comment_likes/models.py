from django.db import models
from users.models import User
# Create your models here.
class CommentLike(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment_likes',null=True)
    comment = models.ForeignKey('comments.Comment',on_delete=models.CASCADE,related_name='comment_likes',null=True)
    