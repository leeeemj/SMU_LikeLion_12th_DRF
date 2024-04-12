from rest_framework import serializers
from comment_likes.models import CommentLike
from posts.serializers import PostSerializer
from users.serializers import *

class CommentLikeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    post=PostSerializer()


    class Meta:
        model=CommentLike
        fields='__all__' 
        