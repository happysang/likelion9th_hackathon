from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'email', 'name', 'phone_number', 'point', 'ans_auth']

        labels = {
            'username' : '아이디',
            'name' : '이름',
            'email' : '이메일',
            'cert' : '인증서',
            'h_name' : '병원 명',
            'phone_number' : '전화 번호',
        }