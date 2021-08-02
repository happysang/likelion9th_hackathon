from django.shortcuts import render
from inner_account.models import CustomUser

# Create your views here.
def home(request):
    return render (request, 'home.html')


def myscrap(request,user_id):  
    user = CustomUser.objects.get(id = user_id)
    post_scraps = user.scrap.all() ##모델의 좋아요 객체와 이름을 같게 해야됨 likes_user
    context={
        "post_scraps":post_scraps,
    }
    return render(request, 'myscrap.html',context)