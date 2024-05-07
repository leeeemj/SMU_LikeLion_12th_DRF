from django.shortcuts import render
from rest_framework.response import Response
from comments.models import Comment
from recomments.models import Recomment
from comments.serializers import CommentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
#답글 작성 
@api_view(['POST'])
def recomment_create(request): 
    if request.method=='POST':
        serializer=CommentSerializer(data=request.data)
        TEST_Comment=Comment.objects.get(id=1)
        if serializer.is_valid():
            serializer.save(post=TEST_Comment)
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
        serializer=CommentSerializer(recomment) #해당 게시물 시리얼라이저에 담기 
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=CommentSerializer(recomment,data=request.data) #수정
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND) 
    elif request.method=='DELETE':
        recomment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
