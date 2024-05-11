from django.shortcuts import render
from rest_framework.response import Response
from comments.models import Comment
from recomments.models import Recomment
from recomments.models import RecommentLike
from recomments.serializers import ReCommentSerializer
from recomments.serializers import ReCommentLikeSerializer
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
#답글 작성 
@api_view(['POST'])
def recomment_create(request,comment_id): 
    try:
        comment=Comment.objects.get(id=comment_id) #댓글 달고자하는 게시물 존재 확인
    except Comment.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer=ReCommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user,comment=comment) #post 객체를 넘겨야 함 
        return Response(serializer.data,status=status.HTTP_201_CREATED)
        
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   

#답글 수정, 삭제, 보기
@api_view(['GET','PUT','DELETE'])
def recomment_detail(request,pk):
    try:
        recomment=Recomment.objects.get(id=pk)
    except Comment.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=ReCommentSerializer(recomment) #해당 게시물 시리얼라이저에 담기 
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=ReCommentSerializer(recomment,data=request.data) #수정
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND) 
    elif request.method=='DELETE':
        recomment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#답글 좋아요 
@api_view(['POST','DELETE'])
def recomment_like(request,pk):
    try:
        recomment = Recomment.objects.get(id=pk)
    except Recomment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    recommentlike=RecommentLike.objects.create(user=pk,recomment=recomment)
    if request.method=='POST':
        serializer=ReCommentLikeSerializer(recommentlike)
        return Response(serializer,status=status.HTTP_201_CREATED)
    elif request.method=='DELETE':
        recommentlike.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   
