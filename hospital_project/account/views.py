from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout

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
        # else: return redirect('urllogin') 로그인이 잘 안됐을 때 나올 view
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'view_loginform':form})


def signup_view(request):
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_user = signup_form.save()
            login(request, signup_user)
            return redirect ('urlhome')
        else: # 회원가입이 잘 안됐을 때 나올 view
            form = UserCreationForm()
            return render (request, 'signup.html', {'view_signupform':form})
    else:
        form = UserCreationForm()
        return render (request, 'signup.html', {'view_signupform':form})