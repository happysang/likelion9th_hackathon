from review.models import Review
from question.models import Question
from information.models import Information
from django.shortcuts import render
from inner_account.models import CustomUser
from django.db.models import Q

# Create your views here.
def home(request):
    return render (request, 'home.html')

def myscrap(request,user_id):  
    user = CustomUser.objects.get(id = user_id)
    review_scraps = user.rscrap.all().order_by('-date') ##가져오고자 하는 모델의 컬럼 이름과 같아야함
    question_scraps = user.qscrap.all().order_by('-date')
    info_scraps = user.iscrap.all().order_by('-date')
    context={
        "review_scraps":review_scraps, "question_scraps":question_scraps, "info_scraps":info_scraps
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
    informations = Information.objects.all()
    information_list = informations.filter(user_id=request.user.username)
    return render(request, 'myobject.html',{'review_list':review_list, 'question_list':question_list, 'information_list':information_list,})

def all_search_view(request):
    rsearch_all = Review.objects.all()
    qsearch_all = Question.objects.all()
    infosearch_all = Information.objects.all()
    q = request.POST.get('q', "")
    if q:
        search_all = rsearch_all.filter(Q(title__icontains=q) | Q(body__icontains=q))
        return render(request, 'all_search.html', {'search_all':search_all, 'q':q})
    if q:
        search_all = qsearch_all.filter(Q(title__icontains=q) | Q(body__icontains=q))
        return render(request, 'all_search.html', {'search_all':search_all, 'q':q})
    if q:
        search_all = infosearch_all.filter(Q(title__icontains=q) | Q(body__icontains=q))
        return render(request, 'all_search.html', {'search_all':search_all, 'q':q})
    else:
        return render(request, 'all_search.html')