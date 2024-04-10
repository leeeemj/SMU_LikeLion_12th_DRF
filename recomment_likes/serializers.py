from rest_framework import serializers
from recomment_likes.models import RecommentLike
from recomments.serializers import ReCommentSerializer
from users.serializers import *

class CommentLikeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    recomment =ReCommentSerializer()


    class Meta:
        model=RecommentLike
        fields='__all__' #댓글 좋아요에선 가져올게 없는데 all...?