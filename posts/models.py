from django.db import models
from users.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts',null=True)
    title=models.CharField(max_length=50,null=True)
    content=models.CharField(max_length=500,null=True,blank=True)
    is_comment=models.BooleanField(null=False,default=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='posts/', height_field=200, width_field=200, max_length=None,null=True)
    location_tag=models.CharField(max_length=50,null=True)