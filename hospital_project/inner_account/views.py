from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from inner_account.forms import NormalForm, DoctorForm
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        auth_form = AuthenticationForm(request=request, data = request.POST)
        if auth_form.is_valid():
            auth_username = auth_form.cleaned_data.get("username")
            auth_password = auth_form.cleaned_data.get("password")
            auth_user = authenticate(request=request, username=auth_username, password = auth_password)
            login(request, auth_user)
            return redirect('urlhome')
        else:
            messages.warning(request, '잘못된 정보입니다.') #로그인이 잘 안됐을 때 나올 view
            return redirect('urllogin')

    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'view_loginform':form})

def choice(request):
    return render (request, 'choice.html')


def signup_view(request,c):
    if request.method == 'POST':
        if c == '1':
            signup_form = NormalForm(request.POST, request.FILES)
            if signup_form.is_valid():
                signup_user = signup_form.save(commit=False)
                signup_user.point = 0
                signup_user.ans_auth = False
                signup_user.save()
                login(request, signup_user)
                return redirect ('urlhome')
        if c == '2':
            signup_form = DoctorForm(request.POST, request.FILES)
            if signup_form.is_valid():
                signup_user = signup_form.save(commit=False)
                signup_user.point = 300
                signup_user.ans_auth = False #추후 파일을 보고 True로 변경해준다.
                signup_user.save()
                login(request, signup_user)
                return redirect ('urlhome')
        # else: # 회원가입이 잘 안됐을 때 나올 view
        #     form = RegisterForm()
        #     return render (request, 'signup.html', {'view_signupform':form})
    else:
        if c == '1':
            form = NormalForm()
            return render (request, 'signup.html', {'n_view_signupform':form})
        if c == '2':
            form = DoctorForm()
            return render (request, 'signup.html', {'d_view_signupform':form})

def logout_view(request):
    logout(request)
    return redirect ('urlhome')
