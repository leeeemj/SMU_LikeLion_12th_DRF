from django.shortcuts import render
from rest_framework.response import Response
from comments.models import Comment
from recomments.models import Recomment
from recomments.models import RecommentLike
from recomments.serializers import ReCommentSerializer
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.
#답글 작성 
@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
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
@permission_classes([IsAuthenticatedOrReadOnly])
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
        return Response(serializer.data,status=status.HTTP_404_NOT_FOUND) 
    elif request.method=='DELETE':
        recomment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#좋아요 생성 및 삭제 
@api_view(['POST','DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def recomment_like(request,recomment_id):
    try:
        recomment=Recomment.objects.get(id=recomment_id)
    except Recomment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='POST':
        if RecommentLike.objects.filter(user=request.user, recomment=recomment).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            recommentlike=RecommentLike.objects.create(user=request.user,recomment=recomment) #objects.create 사용하거나 serializer 사용해서 생성 가능함
            return Response(status=status.HTTP_201_CREATED)
    
    elif request.method=='DELETE':
        recommentlike=RecommentLike.objects.get(user=request.user, recomment=recomment)
        recommentlike.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)