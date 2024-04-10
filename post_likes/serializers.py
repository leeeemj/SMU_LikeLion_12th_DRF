from rest_framework import serializers
from post_likes.models import PostLike
from posts.serializers import PostSerializer
from users.serializers import *

class CommentLikeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    post=PostSerializer()


    class Meta:
        model=PostLike
        fields='__all__' 
        