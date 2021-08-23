from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User # auth_user 테이블과 연결된 모델


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일") #기본 email의 형식 검사
    # last_name = forms.CharField(label='닉네임')
    last_name = forms.CharField(max_length=30, required=False)
    class Meta: # 클래스의 원천 클래스(클래스 설명 클래스) - 현 class가 연결해야할 model 정의
        model = User
        fields = ("username","last_name", "email",) # 사용할 필드면 명사(id, password는 기본 포함) - 필드명과 template에서 넘어오는 name 속성은 동일해야 함