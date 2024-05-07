from django.shortcuts import render
from rest_framework.response import Response
from recomments.models import Recomment
from posts.serializers import PostSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from recomment_likes.models import RecommentLike
# Create your views here.

#좋아요 생성 및 삭제 
@api_view(['POST','DELETE'])
def recomment_like(request,pk):
    try:
        recomment = Recomment.objects.get(id=pk)
    except Recomment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    recommentlike=RecommentLike.objects.create(user=pk,recomment=recomment)
    if request.method=='POST':
        serializer=PostSerializer(recommentlike)
        return Response(serializer,status=status.HTTP_201_CREATED)
    elif request.method=='DELETE':
        recommentlike.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)