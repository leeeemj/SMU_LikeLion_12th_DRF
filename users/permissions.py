from rest_framework import permissions 

class IsUserOwner(permissions.BasePermission):
    # def has_permission(self, request, view):
    #     if (request.method=='POST') or (request.method=='GET'): #회원가입과 로그인은 인증된 사용자 아니어도 되도록
    #         return True
    #     return bool(request.user and request.user.is_authenticated)
    #user에선 has_permission 필요 없을 듯 

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: #GET,HEAD 등 db 건들지 않는 것들 
            return True
        return obj.user_id == request.user