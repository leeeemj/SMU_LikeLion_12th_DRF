from django.shortcuts import render
from rest_framework.response import Response
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework import status
# Create your views here.

#게시물리스트
@api_view(['GET','POST']) #허용할 메소드 
def post_list(request):
    if request.method=='GET': #가져오기
        posts=Post.objects.all() #model Post의 모든 객체 가져오기
        serializer=PostSerializer(posts,many=True) #posts라는 객체를 직렬화하고 여러 객체를 직렬화한다. many=True : 객체가 여러개일때 
        return Response(serializer.data)
    elif request.method=='POST': #생성하기 (게시물 리스트에 추가하기)
        #요청 통해 들어온 자원 serializer 해줘야함 -> get과는 반대 방향으로 직렬화 
        #누가 생성했는데 user가 필요함 ->외래키 직접 설정해주어야함 
        serializer=PostSerializer(data=request.data, user=request.user) #한번에 한개 쓸거니까 many 필요 없을 듯 
        
        if serializer.is_valid():
            serializer.save() #값 유효하면 저장, 저장해서 db update
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

#게시물 내용 
@api_view(['GET','PUT','DELETE'])
def post_detail(request,pk): #여기선 pk = user id 
    ##세미나때 일단 아무 유저가 get 통해서 사용하라 하셨는데 어떻게 해야되는건지 모르겠습니다 ... 
    #pk 있는 함수에서는 예외처리를 해줘야 한다. 
    try:
        post=Post.objects.get(pk=pk)
        #해당 게시물의 유저가 동일한 객체 넘겨 받는 ..? 
        ## 해당 유저가 쓴 게시물이 여러개면 어떻게 하는건가요 ??
        ### 아 특정 게시물에서 요청받는거니까 딱히 상관 없는건가요 ? 
        #### post=Post.objects.get(pk=pk) 코드가 정확히 어떻게 되는건지 잘 모르겠습니다 ...
    except Post.DoesNotExist: #해당 유저가 쓴 게시물 없으면 404 
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=PostSerializer(post) #해당 게시물 시리얼라이저에 담기 
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=PostSerializer(post,data=request.data) #수정
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND) 
    elif request.method=='DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
        
        