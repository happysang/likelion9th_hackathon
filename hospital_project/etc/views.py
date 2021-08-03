from review.models import Review
from question.models import Question
from information.models import Info
from django.shortcuts import render
from inner_account.models import CustomUser

# Create your views here.
def home(request):
    return render (request, 'home.html')

def myscrap(request,user_id):  
    user = CustomUser.objects.get(id = user_id)
    post_scraps = user.scrap.all() ##가져오고자 하는 모델의 컬럼 이름과 같아야함
    post_scraps = post_scraps.order_by('-date')
    context={
        "post_scraps":post_scraps,
    }
    return render(request, 'myscrap.html',context)

def mypage(request):
    return render(request,'mypage.html')

def mypagedetail(request):
    return render(request, 'mypagedetail.html')

def myobject(request):
    reviews = Review.objects.all()
    review_list = reviews.filter(user_id=request.user.username)
    questions = Question.objects.all()
    question_list = questions.filter(user_id=request.user.username)
    informations = Info.objects.all()
    information_list = informations.filter(user_id=request.user.username)
    return render(request, 'myobject.html',{'review_list':review_list, 'question_list':question_list, 'information_list':information_list,})
