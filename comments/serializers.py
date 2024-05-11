from rest_framework import serializers
from comments.models import Comment
from comments.models import CommentLike
from posts.serializers import PostSerializer
from recomments.models import Recomment
from users.serializers import *

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    post =PostSerializer(required=False)

    #답글 수 
    recomment_num=serializers.SerializerMethodField()
    #댓글 좋아요 수 
    comment_like_num=serializers.SerializerMethodField()

    class Meta:
        model=Comment
        # exclude = ('user','post')
        fields='__all__'
        
    def get_recomment_num(self,obj): 
        return Recomment.objects.filter(comment=obj).count()
    
    def get_comment_like_num(self,obj): 
        return CommentLike.objects.filter(comment=obj).count()
    
class CommentLikeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    comment =CommentSerializer()


    class Meta:
        model=CommentLike
        fields='__all__' #댓글 좋아요에선 가져올게 없는데 all...?