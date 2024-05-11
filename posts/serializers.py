from comments.models import Comment
from rest_framework import serializers
from posts.models import Post
from posts.models import PostLike
from users.serializers import *


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    posts_like_num=serializers.SerializerMethodField()
    comments_num=serializers.SerializerMethodField()
    class Meta:
        model=Post
        fields='__all__'

    
    def get_posts_like_num(self,obj): 
        return PostLike.objects.filter(post=obj).count()
    #PostLike를 count하려면 한 게시물에 여러 사용자가 누른걸 세야함 

    def get_comments_num(self,obj): 
        return Comment.objects.filter(post=obj).count()

class PostLikeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    post = PostSerializer()


    class Meta:
        model=PostLike
        fields='__all__'