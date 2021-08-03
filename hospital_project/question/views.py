from .models import Question
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import CommentForm

# Create your views here.

d_list = ['치과', '피부과', '성형외과', '산부인과', '안과', '내과', '외과', '이비인후과', '정형외과',
            '비뇨기과', '정신건강의학과', '재활의학과', '영상의학과', '소아과', '신경외과', '신경과',
            '마취통증의학과', '가정의학과', '한의원', '모든 진료과']

def question_category_view(request):
    return render (request, 'question_category.html')
    
def question_readall_view(request, d_num):
    for x in range(len(d_list)):
        if d_num == x:
            qusetions = Question.objects.all()
            question_list = qusetions.filter(dept=d_list[x])
            question_all = question_list.order_by("-date")
            d_name = d_list[x]
            return render(request,"question_readall.html",{'views_question_all':question_all, 'd_num':d_num, 'd_name':d_name},)    

def question_detail_view(request, id):
    question = get_object_or_404(Question,pk= id)
    #조회수 기능
    default_view_count = question.view_count
    question.view_count = default_view_count +1 
    question.save()
    for x in range(len(d_list)):
        if d_list[x] == question.dept:
            d_num = x
    return render(request,'question_detail.html',{'views_question':question, 'd_num':d_num})

def question_new_view(request, d_num):
    for x in range(len(d_list)):
        if x == d_num:
            d_name = d_list[x]
            break
    return render(request, 'question_new.html', {'d_num':d_num, 'd_name':d_name})

def question_create_view(request, d_num):
    if request.method == 'POST':
        cquestion = Question()
        cquestion.title = request.POST['ctitle']
        cquestion.user_id = request.POST['cuser_id']
        cquestion.dept = request.POST['cdept']
        cquestion.body = request.POST['cbody']
        cquestion.date = timezone.now()
        cquestion.save()
        return redirect('urlquestionreadall', d_num)
    else:
        return render(request,'question_new.html')

def question_edit_view(request, id):
    ereview = Question.objects.get(id = id)
    return render(request, 'question_edit.html', {'views_equestion': ereview})

def question_update_view(request, id):
    uquestion = Question.objects.get(id = id)
    uquestion.title = request.POST['utitle']
    uquestion.user_id = request.POST['user_id']
    uquestion.dept = request.POST['udept']
    uquestion.body = request.POST['ubody']
    uquestion.date = timezone.now()
    uquestion.save()
    return redirect('urlquestiondetail', uquestion.id)

def question_delete_view(request, id):
    dquestion = Question.objects.get(id = id)
    for x in range(len(d_list)):
        if d_list[x] == dquestion.dept:
            d_num = x    
    dquestion.delete()
    return redirect('urlquestionreadall', d_num)

def add_comment(request, id): 
    question=get_object_or_404(Question, pk=id) 
    if request.method == "POST":
         form=CommentForm(request.POST) 
         if form.is_valid(): 
             comment=form.save(commit=False) 
             comment.post= question 
             comment.save() 
         return redirect('urlquestiondetail',id) 
    else: 
        form=CommentForm() 
    return render(request, 'add_comment.html', {'form':form})

import json
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Question


@login_required
@require_POST
def like(request):
    pk = request.POST.get('pk', None)
    object = get_object_or_404(Question, pk=pk)
    user = request.user

    if object.like.filter(id=user.id).exists():
        object.like.remove(user)
        message = '좋아요가 취소되었습니다.'
    else:
        object.like.add(user)
        message = '좋아요를 누르셨습니다.'

    context = {'likes_count':object.like.count(), 'message': message}
    return HttpResponse(json.dumps(context), content_type="application/json")

def fun(request):
    pk = request.POST.get('pk', None)
    object = get_object_or_404(Question, pk=pk)
    user = request.user

    if object.fun.filter(id=user.id).exists():
        object.fun.remove(user)
        message = '재밌어요가 취소되었습니다.'
    else:
        object.fun.add(user)
        message = '재밌어요를 누르셨습니다.'

    context = {'funs_count':object.fun.count(), 'message': message}
    return HttpResponse(json.dumps(context), content_type="application/json")

def upset(request):
    pk = request.POST.get('pk', None)
    object = get_object_or_404(Question, pk=pk)
    user = request.user

    if object.upset.filter(id=user.id).exists():
        object.upset.remove(user)
        message = '불쾌해요가 취소되었습니다.'
    else:
        object.upset.add(user)
        message = '불쾌해요를 누르셨습니다.'

    context = {'upsets_count':object.upset.count(), 'message': message}
    return HttpResponse(json.dumps(context), content_type="application/json")


def scrap(request):
    pk = request.POST.get('pk', None)
    object = get_object_or_404(Question, pk=pk)
    user = request.user

    if object.scrap.filter(id=user.id).exists():
        object.scrap.remove(user)
        message = '스크랩이 취소되었습니다.'
    else:
        object.scrap.add(user)
        message = '스크랩 하셨습니다.'

    context = {'scraps_count':object.scrap.count(), 'message': message}
    return HttpResponse(json.dumps(context), content_type="application/json")