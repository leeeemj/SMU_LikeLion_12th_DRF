from rest_framework import serializers
from comment_likes.models import CommentLike
from comments.models import Comment
from posts.serializers import PostSerializer
from recomments.models import Recomment
from users.serializers import *

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    post =PostSerializer()

    #답글 수 
    recomment_num=serializers.SerializerMethodField()
    #댓글 좋아요 수 
    comment_like_num=serializers.SerializerMethodField()

    class Meta:
        model=Comment
        fields='__all__'
        
    def get_recomments_num(self,obj): 
        return Recomment.objects.filter(comment=obj).count()
    
    def get_comment_like_num(self,obj): 
        return CommentLike.objects.filter(comment=obj).count()