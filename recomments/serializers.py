from rest_framework import serializers
from users.serializers import *
from comments.serializers import CommentSerializer
from recomments.models import Recomment
from recomments.models import RecommentLike


class ReCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    comment=CommentSerializer()
    
    #답글 좋아요 수 
    recomment_like_num=serializers.SerializerMethodField()

    class Meta:
        model=Recomment
        fields='__all__'

    def get_recomment_like_num(self,obj): 
        return RecommentLike.objects.filter(recomment=obj).count()
    

class ReCommentLikeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    recomment =ReCommentSerializer()
    class Meta:
        model=RecommentLike
        fields='__all__'