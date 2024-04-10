from rest_framework import serializers
from comment_likes.models import CommentLike
from comments.serializers import CommentSerializer
from users.serializers import *

class CommentLikeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    comment =CommentSerializer()


    class Meta:
        model=CommentLike
        fields='__all__' #댓글 좋아요에선 가져올게 없는데 all...?
        