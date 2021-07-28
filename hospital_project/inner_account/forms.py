from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'email', 'name', 'phone_number']

        labels = {
            'username' : '아이디',
            'password1' : '비밀번호',
            'password2' : '비밀번호 확인',
            'name' : '이름',
            'email' : '이메일',
            'phone_number' : '전화 번호',
        }

class DoctorForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'email', 'name', 'phone_number', 'h_name', 'cert']
        labels = {
            'username' : '아이디',
            'password1' : '비밀번호',
            'password2' : '비밀번호 확인',
            'name' : '이름',
            'email' : '이메일',
            'phone_number' : '전화 번호',
            'h_name' : '병원 명',
            'cert' : '의사 인증 파일 제출',
        }