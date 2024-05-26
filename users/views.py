from django.shortcuts import render
from rest_framework.response import Response
from posts.models import Post
from users.serializers import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view
# from rest_framework.decorators.action 
from users.models import User
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from .permissions import IsUserOwner
from django.shortcuts import get_object_or_404
 
# Create your views here.

#회원가입
@api_view(['POST'])
def user_join(request):
    if request.method=='POST':
        # username=request.data.get('username')
        # password=request.data.get('password')
        # user=User.objects.create_user(username=username,password=password)
        #위에것과 유저시리얼라이저의 create_user가 중복되어서 이미 존재하는 사용자 오류가 떴었음. 둘 중 하나만 하기
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        #username,email,password 다 안 넣어서 생기는 오류 처리 생각하기 

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
            # serializer.save()
            #비번수정한게 반영이 x -> 수정하고 로그인하면 401에러 발생
            #비번은 따로 처리 필요
            # password write_only 설정-> set_password 사용 (암호화하여 저장)
            user=serializer.save() #생성된 모델 인스턴스가 user에 저장 , 직렬화된 데이터 저장이 아님
            if 'modify_pw' in request.data:
                user.set_password(request.data['modify_pw']) #user로 해결하면 되는 것
                user.save()
            return Response(serializer.data)
            #비밀번호 수정 가능해짐
            #PUT할 때 비밀번호 필수임
            #pw에 다른 번호 넣으면 수정되어버림 -> 비밀번호 확인하는 절차가 소용없어짐 
            #확인용 pw와 수정용 pw를 받아서 처리..? ->ㅇㅇ됐음
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND) 
    elif request.method=='DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def user_login(request):
    username=request.data.get('username')
    password=request.data.get('password')

    user=User.objects.get(username=username)
    #user.password는 암호화된 상태 
    if not check_password(password,user.password):
        return Response({'비번 틀림'},status=status.HTTP_401_UNAUTHORIZED)
    #토큰 발급 과정 
    token=RefreshToken.for_user(user) #토큰 발급 방법 여러개 중 하나
    serializer=UserSerializer(user)
    return Response(
        status=status.HTTP_200_OK,
        data={
            'token':str(token.access_token), #위의 token과 다름 
            'user':serializer.data,
        }
    )
#access토큰 : 로그인할 때 인증하게 되는 토큰
#refresh토큰은 토큰을 갱신하기 위한 ..? 이게 더 수명 길다. 
# @api_view(['GET'])
# def test_login(request):
#     if request.user.is_authenticated:
#         serializer=UserSerializer(request.user)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     return Response(status=status.HTTP_401_UNAUTHORIZED)

#viewset

class UserViewSet(viewsets.ModelViewSet):
    permission_classes=[IsUserOwner]
    
    queryset=User.objects.all()
    serializer_class=UserSerializer
    lookup_field='id'
    lookup_url_kwarg='user_id'
    
    #get_object를 해야 has_object_permission 가능
    def get_object(self):
        return super().get_object()

    @action(methods=['POST'],detail=False,url_path='login',url_name='user_login')
    def user_login(self,request):
        username=request.data.get('username')
        password=request.data.get('password')

        user=User.objects.get(username=username)
        #user.password는 암호화된 상태 
        if not check_password(password,user.password):
            return Response({'비번 틀림'},status=status.HTTP_401_UNAUTHORIZED)
        #토큰 발급 과정 
        token=RefreshToken.for_user(user) #토큰 발급 방법 여러개 중 하나
        serializer=UserSerializer(user)
        return Response(
            status=status.HTTP_200_OK,
            data={
                'token':str(token.access_token), #위의 token과 다름 
                'user':serializer.data,
            }
        )
    

    
