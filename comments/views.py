from django.shortcuts import render
from rest_framework.response import Response
from comments.models import Comment
from recomments.models import Recomment
from posts.models import Post
from comments.serializers import CommentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['POST'])
def comment_create(request,pk): 
    try:
        post=Post.objects.get(id=pk)
    except Post.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)
    # if request.method=='POST':
    #     serializer=CommentSerializer(request.data)
    #     TEST_POST=Post.objects.get(id=1)
    #     if serializer.is_valid():
    #         serializer.save(post=TEST_POST)
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    # else:   
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(post=post)  # 직접 가져온 post 객체를 사용하여 댓글 저장
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#댓글 수정, 삭제, 보기
@api_view(['GET','PUT','DELETE'])
def comment_detail(request,pk):
    try:
        comment=Comment.objects.get(id=pk)
    except Comment.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=CommentSerializer(comment) #해당 게시물 시리얼라이저에 담기 
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=CommentSerializer(comment,data=request.data) #수정
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND) 
    elif request.method=='DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#답글가져오기
#게시물 댓글 가져오기 
@api_view(['GET'])
def recomment_list(request,pk):
    try:
        comment=Comment.objects.get(id=pk)
    except Post.DoesNotExist: #해당 유저가 쓴 게시물 없으면 404 
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        recomments=Recomment.objects.fillter(comment=comment)
        serializer=CommentSerializer(recomments,many=True)
        return Response(serializer.data)
    
