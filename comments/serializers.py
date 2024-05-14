from rest_framework import serializers
from comments.models import Comment
from comments.models import CommentLike
from posts.serializers import PostSerializer
from recomments.models import Recomment
from users.serializers import *

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True) #관계된 객체 ID만 반환
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    #serializer.save(user=request.user,post=post)할 때 들어오는 user와 post가 저장된다.
    # PrimaryKeyrelatedField() => 연결되어 있는 collection 자동으로 찾아줌 
    
    # user = UserSerializer(required=False) # required=False => 해당 필드 필수 아님
    # post =PostSerializer(required=False)
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
        fields='__all__' 