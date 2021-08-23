from django.contrib.auth import authenticate, login #  login 모듈, authenticate 인증객체 생성
from django.shortcuts import render, redirect
from accounts.forms import UserForm

def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid(): # form의 접속이 유지되어 있으면
            form.save() # db에 저장
            # 가입한 회원으로 로그인 처리
            username = form.cleaned_data.get('username') # cleaned_data(네트워크 데이터가 아닌 db를 저장하기 위해 정제한 data)
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password ) # 인증객체 생성
            login(request, user) # 로그인 처리
            return redirect('http://127.0.0.1:8000') # main 컨텐츠 호출(authenticated 정보가 같이 전달됨)
    else:
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})

