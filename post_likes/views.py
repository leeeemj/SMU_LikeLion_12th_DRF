from django.shortcuts import render
from rest_framework.response import Response
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from post_likes.models import PostLike
# Create your views here.

#좋아요 생성 및 삭제 
@api_view(['POST','DELETE'])
def post_like(request,pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    postlike=PostLike.objects.create(user=pk,post=post)
    if request.method=='POST':
        serializer=PostSerializer(postlike)
        return Response(serializer,status=status.HTTP_201_CREATED)
    elif request.method=='DELETE':
        postlike.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)