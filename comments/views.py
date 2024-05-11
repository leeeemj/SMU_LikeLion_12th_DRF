from django.shortcuts import render
from rest_framework.response import Response
from comments.models import Comment
from comments.models import CommentLike
from recomments.models import Recomment
from posts.models import Post
from comments.serializers import CommentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['POST'])
def comment_create(request,post_id): 
    #인증 되었는지 확인 
    # if not request.user.is_authenticated:
    #     return Response({"detail": "로그인 필요"}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        post=Post.objects.get(id=post_id) #댓글 달고자하는 게시물 존재 확인
    except Post.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer=CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user,post=post) #post 객체를 넘겨야 함 
        return Response(serializer.data,status=status.HTTP_201_CREATED)
        #게시물 댓글에 게시물 전체 내용까지 저장될 필요는 없는 것 같음 
        ##간단하게 추려도 되나여 ?? 
        
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#댓글 수정, 삭제, 보기
@api_view(['GET','PUT','DELETE'])
def comment_detail(request,comment_id):
    try:
        comment=Comment.objects.get(id=comment_id)
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

#댓글에 대한 답글 리스트 가져오기 
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
    
#좋아요 생성 및 삭제 
@api_view(['POST','DELETE'])
def comment_like(request,comment_id):
    try:
        comment=Comment.objects.get(id=comment_id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='POST':
        if CommentLike.objects.filter(user=request.user, comment=comment).exists():
            return Response({'좋아요 이미 존재'},status=status.HTTP_400_BAD_REQUEST)
        else:
            commentlike=CommentLike.objects.create(user=request.user,comment=comment) #objects.create 사용하거나 serializer 사용해서 생성 가능함
            return Response({'좋아요'},status=status.HTTP_201_CREATED)
    
    elif request.method=='DELETE':
        commentlike=CommentLike.objects.get(user=request.user, comment=comment)
        commentlike.delete()
        return Response({'좋아요 삭제'},status=status.HTTP_204_NO_CONTENT)
        