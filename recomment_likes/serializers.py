from rest_framework import serializers
from recomment_likes.models import RecommentLike
from recomments.serializers import ReCommentSerializer
from users.serializers import *

class ReCommentLikeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    recomment =ReCommentSerializer()


    class Meta:
        model=RecommentLike
        fields='__all__'