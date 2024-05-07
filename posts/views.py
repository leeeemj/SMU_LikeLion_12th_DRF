from django.shortcuts import render
from rest_framework.response import Response
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from users.models import User
from comments.models import Comment
from comments.serializers import CommentSerializer
# Create your views here.

#게시물리스트
@api_view(['GET','POST']) #허용할 메소드 
def post_list(request):
    if request.method=='GET': #가져오기
        posts=Post.objects.all() #model Post의 모든 객체 가져오기
        serializer=PostSerializer(posts,many=True) #posts라는 객체를 직렬화하고 여러 객체를 직렬화한다. many=True : 객체가 여러개일때 
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='POST': #생성하기 (게시물 리스트에 추가하기)
        #요청 통해 들어온 자원 serializer 해줘야함 -> get과는 반대 방향으로 직렬화 
        #누가 생성했는데 user가 필요함 ->외래키 직접 설정해주어야함 
        serializer=PostSerializer(data=request.data) #한번에 한개 쓸거니까 many 필요 없을 듯 
        TEST_USER=User.objects.get(id=1)
        if serializer.is_valid():
            serializer.save(user=TEST_USER) #값 유효하면 저장, 저장해서 db update
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

#게시물 내용 
@api_view(['GET','PUT','DELETE'])
def post_detail(request,pk): #여기선 pk = postid
    #pk 있는 함수에서는 예외처리를 해줘야 한다. 
    try:
        post=Post.objects.get(id=pk)
    except Post.DoesNotExist: #해당 유저가 쓴 게시물 없으면 404 
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=PostSerializer(post) #해당 게시물 시리얼라이저에 담기 
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=PostSerializer(post,data=request.data) #수정
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND) 
    elif request.method=='DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#게시물 댓글 가져오기 
@api_view(['GET'])
def post_comments(request,pk):
    try:
        post=Post.objects.get(id=pk)
    except Post.DoesNotExist: #해당 유저가 쓴 게시물 없으면 404 
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        comments=Comment.objects.fillter(post=post)
        serializer=CommentSerializer(comments,many=True)
        return Response(serializer.data)
        


    
    
        
        