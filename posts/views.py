from django.shortcuts import render
from rest_framework.response import Response
from posts.models import Post
from posts.models import PostLike
from posts.serializers import PostSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from comments.models import Comment
from comments.serializers import CommentSerializer
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import viewsets
# Create your views here.

#게시물리스트 + 게시물 생성
@api_view(['GET','POST']) 
def post_list(request):
    if request.method=='GET': 
        posts=Post.objects.all() 
        serializer=PostSerializer(posts,many=True) 
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='POST': 
        serializer=PostSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#게시물 내용 
#게시물 쓴 사람만이 put,delete 가능하도록 하려면
#login_required or PermissionRequiredMixin 사용 
@api_view(['GET','PUT','DELETE'])
def post_detail(request,post_id): #여기선 pk = postid
    #pk 있는 함수에서는 예외처리를 해줘야 한다. 
    try:
        post=Post.objects.get(id=post_id)
    except Post.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=PostSerializer(post) #해당 게시물 시리얼라이저에 담기 
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer=PostSerializer(post,data=request.data) #수정
        if serializer.is_valid():
            try:
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': '서버 내부 오류가 발생했습니다. 관리자에게 문의해주세요.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND) #errors에 오류정보 담겨 있음  
    elif request.method=='DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    #자꾸 슬래시 빼먹어서 오류남 
    #http://127.0.0.1:8000/posts/6/  

#내가 작성한 게시물 조회 만들기 -> 댓글 되면 ..

#게시물 댓글 가져오기 
@api_view(['GET'])
def post_comments(request,post_id):
    try:
        post=Post.objects.get(id=post_id)
    except Post.DoesNotExist: #해당 유저가 쓴 게시물 없으면 404 
        return Response(status=status.HTTP_404_NOT_FOUND)
    comments=Comment.objects.filter(post=post_id)
    serializer=CommentSerializer(comments,many=True)
    return Response(serializer.data)
        
#좋아요 생성 및 삭제 
@api_view(['POST','DELETE'])
def post_like(request,post_id):
    try:
        post=Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='POST':
        if PostLike.objects.filter(user=request.user, post=post).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            postlike=PostLike.objects.create(user=request.user,post=post) #objects.create 사용하거나 serializer 사용해서 생성 가능함
            return Response(status=status.HTTP_201_CREATED)
    
    elif request.method=='DELETE':
        postlike=PostLike.objects.get(user=request.user, post=post)
        postlike.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#generics ver

#게시물리스트 조회 및 생성
class PostListView(ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer


#게시물 detail
class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    lookup_field='id'
    lookup_url_kwarg='post_id' #retrieve니까 필요 
    #kwarg에 url파라디터 담겨 있음 
    #self.kwargs != **kwargs
    
# class PostViewSet(viewsets.ModelViewSet):
#     queryset=Post.objects.all()
#     serializer_class=PostSerializer
    
    
        
        