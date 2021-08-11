from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from inner_account.forms import NormalForm, DoctorForm
from django.contrib import messages
from .models import CustomUser

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
            if CustomUser.objects.filter(username = request.POST['username']).exists(): #로그인이 잘 안됐을 때 나올 view
                messages.info(request, '비밀번호가 틀렸습니다.')
                return redirect('urllogin')
            else:
                messages.info(request, '존재하지 않는 계정입니다.')
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
            else:
                 # 회원가입이 잘 안됐을 때 나올 view
                if CustomUser.objects.filter(username = request.POST['username']).exists():
                    messages.info(request, '중복된 아이디가 있습니다.')
                    return redirect('urlsignup', c)
            
                elif request.POST['password1'] != request.POST['password2']:
                    messages.info(request, '비밀번호와 비밀번호 확인이 일치하지 않습니다.')
                    return redirect('urlsignup', c)

                elif len(request.POST['password1']) < 8:
                    messages.info(request, '비밀번호는 8자리 이상으로 작성해주세요.')
                    return redirect('urlsignup', c )

                elif request.POST['password1'].isdigit():
                    messages.info(request, '비밀번호는 숫자로만 이루어질 수 없습니다')
                    return redirect('urlsignup', c )

                elif request.POST['username'] in request.POST['password1']:
                    messages.info(request, '비밀번호에 아이디가 포함될 수 없습니다')
                    return redirect('urlsignup', c )
                elif not request.POST['email']:
                    messages.info(request, '이메일을 작성해주세요.')
                    return redirect('urlsignup', c )
                elif not request.POST['name']:
                    messages.info(request, '이름을 작성해주세요.')
                    return redirect('urlsignup', c )
                else:
                    messages.info(request, '알 수 없는 오류입니다. 관리자 문의 : 010-9398-2668')
                    return redirect('urlsignup', c )

        if c == '2':
            signup_form = DoctorForm(request.POST, request.FILES)

            if signup_form.is_valid():
                if not request.POST['cert']:
                    messages.info(request, '의사 증빙 파일을 첨부해주세요.')
                    return redirect('urlsignup', c )
                signup_user = signup_form.save(commit=False)
                signup_user.point = 300
                signup_user.ans_auth = False #추후 파일을 보고 True로 변경해준다.
                signup_user.save()
                login(request, signup_user)
                return redirect ('urlhome')
            else:
                 # 회원가입이 잘 안됐을 때 나올 view
                if CustomUser.objects.filter(username = request.POST['username']).exists():
                    messages.info(request, '중복된 아이디가 있습니다.')
                    return redirect('urlsignup', c)
            
                elif request.POST['password1'] != request.POST['password2']:
                    messages.info(request, '비밀번호와 비밀번호 확인이 일치하지 않습니다.')
                    return redirect('urlsignup', c)

                elif len(request.POST['password1']) < 8:
                    messages.info(request, '비밀번호는 8자리 이상으로 작성해주세요.')
                    return redirect('urlsignup', c )

                elif request.POST['password1'].isdigit():
                    messages.info(request, '비밀번호는 숫자로만 이루어질 수 없습니다')
                    return redirect('urlsignup', c )

                elif request.POST['username'] in request.POST['password1']:
                    messages.info(request, '비밀번호에 아이디가 포함될 수 없습니다')
                    return redirect('urlsignup', c )
                elif not request.POST['email']:
                    messages.info(request, '이메일을 작성해주세요.')
                    return redirect('urlsignup', c )
                elif not request.POST['name']:
                    messages.info(request, '이름을 작성해주세요.')
                    return redirect('urlsignup', c )
                elif not request.POST['h_name']:
                    messages.info(request, '병원명을 작성해주세요.')
                    return redirect('urlsignup', c )
                else:
                    messages.info(request, '알 수 없는 오류입니다. 관리자 문의 : 010-9398-2668')
                    return redirect('urlsignup', c )

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
