from django.shortcuts import render
from rest_framework.response import Response
from comments.models import Comment
from posts.serializers import PostSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from comment_likes.models import CommentLike
# Create your views here.

#좋아요 생성 및 삭제 
@api_view(['POST','DELETE'])
def comment_like(request,pk):
    try:
        comment = Comment.objects.get(id=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    commentlike=CommentLike.objects.create(user=pk,comment=comment)
    if request.method=='POST':
        serializer=PostSerializer(commentlike)
        return Response(serializer,status=status.HTTP_201_CREATED)
    elif request.method=='DELETE':
        commentlike.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)