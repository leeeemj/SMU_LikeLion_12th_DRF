from django.shortcuts import render
from rest_framework.response import Response
from posts.models import Post
from users.serializers import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from users.models import User
# Create your views here.

#회원가입
@api_view(['POST'])
def user_join(request):
    if request.method=='POST':
        # username=request.data.get('username')
        # password=request.data.get('password')
        # user=User.objects.create_user(username=username,password=password)
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#회원 정보 수정, 탈퇴, 보기
@api_view(['GET','PUT','DELETE'])
def user_detail(request,pk):
    try:
        user=User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=UserSerializer(user)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=UserSerializer(user,data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND) 
    elif request.method=='DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

