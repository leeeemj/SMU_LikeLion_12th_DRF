from rest_framework import serializers
from posts.models import Post
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    posts_num=serializers.SerializerMethodField()
    class Meta:
        model=User
        ##시리얼라이징할 필드 지정 
        ##전부 지정할 땐 '__all__'
        fields=['id','username','email','password','posts_num'] 
        extra_kwargs={'password':{'write_only':True}}

    def get_posts_num(self,obj): #obj=시리얼라이징한 대상 
        return Post.objects.filter(user=obj).count()