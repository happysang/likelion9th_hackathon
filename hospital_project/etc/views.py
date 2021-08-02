from django.shortcuts import render
from inner_account.models import CustomUser

# Create your views here.
def home(request):
    return render (request, 'home.html')

def mypage(request):
    return render(request,'mypage.html')

def mypagedetail(request):
    return render(request, 'mypagedetail.html')