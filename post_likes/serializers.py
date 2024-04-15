from rest_framework import serializers
from comment_likes.models import CommentLike
from post_likes.models import PostLike
from posts.serializers import PostSerializer
from users.serializers import *

class PostLikeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    post = PostSerializer()


    class Meta:
        model=PostLike
        fields='__all__'
        