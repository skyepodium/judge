from django.shortcuts import render
from django.http import HttpResponse
from user.models import User
# Create your views here.

#class 뷰로 바꾸자
def code_test(request):
    if request.method == "POST":

        #유저 코드 받음
        user_code = request.POST['code']

        #유저 코드 타입
        code_mode = request.POST['codeMode']

        #유저 인증 한번더 거치자
        current_user = request.user

        user_model = User
        user_email = user_model.objects.get(id=current_user.id).email

        print(code_mode)
        print(user_code)
        print(current_user.id)
        print(user_email)

        return HttpResponse('받았음')

    