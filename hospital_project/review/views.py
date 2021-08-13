from typing import ContextManager
from django.core import paginator
from django.http import request
from review.models import Review
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from .forms import CommentForm
from django.db.models import Q
from django.db import connection
from django.shortcuts import render
from django.core.paginator import Paginator


# Create your views here.
d_list = ['치과', '피부과', '성형외과', '산부인과', '안과', '내과', '외과', '이비인후과', '정형외과',
            '비뇨기과', '정신건강의학과', '재활의학과', '영상의학과', '소아과', '신경외과', '신경과',
            '마취통증의학과', '가정의학과', '한의원', '그 외']

def review_category_view(request):
    return render (request, 'review_category.html')


def review_readall_view(request, d_num):
    for x in range(len(d_list)):
        if d_num == x:
            reviews = Review.objects.all()
            review_list = reviews.filter(dept=d_list[x])
            review_all = review_list.order_by("-date")
            d_name = d_list[x]

            paginator = Paginator(review_all,5)
            page = request.GET.get('page')
            posts = paginator.get_page(page)
            
            return render(request,"review_readall.html",{'views_review_all':posts, 'd_num':d_num, 'd_name':d_name})    
    

def review_detail_view(request, id):
    review = get_object_or_404(Review,pk= id)
    default_view_count = review.view_count
    review.view_count = default_view_count +1 
    review.save()
    doctor_name = review.user_id.replace("✔️","")
    for x in range(len(d_list)):
        if d_list[x] == review.dept:
            d_num = x
    comment_form=CommentForm()
    if request.method == "POST":
        form=CommentForm(request.POST) 
        if form.is_valid(): 
            comment=form.save(commit=False)
            if comment.doc == 'doc':
                comment.author_name = "✔️"+request.POST['author_name']
            comment.post= review 
            comment.save() 
        return redirect('urlreviewdetail',id)
    return render(request,'review_detail.html',{'views_review':review, 'd_num':d_num, 'comment_form':comment_form, 'doctor_name':doctor_name})


# def add_comment(request, id): 
#     review=get_object_or_404(Review, pk=id) 
 


def review_new_view(request, d_num):
    for x in range(len(d_list)):
        if x == d_num:
            d_name = d_list[x]
            break
    return render(request, 'review_new.html', {'d_num':d_num, 'd_name':d_name})

def review_create_view(request, d_num):
    if request.method == 'POST':
        creview = Review()
        creview.title = request.POST['ctitle']
        creview.user_id = request.POST['cuser_id']
        creview.hname = request.POST['chname']
        creview.dname = request.POST['cdname']
        creview.dept = request.POST['cdept']
        creview.cert = request.FILES.get('ccert')
        creview.body = request.POST['cbody']
        creview.doc = request.POST.get('doc')
        creview.date = timezone.now()
        if creview.doc == 'doc':
            creview.user_id = "✔️"+request.POST['cuser_id']
        creview.save()
        return redirect('urlreviewreadall', d_num)
    else:
        return render(request,'review_new.html')

def review_edit_view(request, id):
    ereview = Review.objects.get(id = id)
    return render(request, 'review_edit.html', {'views_ereview': ereview})

def review_update_view(request, id):
    ureview = Review.objects.get(id = id)
    ureview.title = request.POST['utitle']
    ureview.user_id = request.POST['uuser_id']
    ureview.hname = request.POST['uhname'] 
    ureview.dname = request.POST['udname']
    ureview.dept = request.POST['udept']
    ureview.cert = request.FILES.get('ucert')
    ureview.body = request.POST['ubody']
    ureview.doc = request.POST.get('doc')
    ureview.date = timezone.now()
    ureview.save()
    return redirect('urlreviewdetail', ureview.id)
    
def review_delete_view(request, id):
    dreview = Review.objects.get(id = id)
    for x in range(len(d_list)):
        if d_list[x] == dreview.dept:
            d_num = x    
    dreview.delete()
    return redirect('urlreviewreadall', d_num)

def review_search_view(request):
    sreview = Review.objects.all()
    q = request.POST.get('q', "")
    if q:
        sreview = sreview.filter(Q(title__icontains=q) | Q(body__icontains=q))
        c = sreview.count()
        return render(request, 'review_search.html', {'sreview':sreview, 'q':q, 'count':c})
    else:
        return render(request, 'review_search.html')

    
import json
from django.http import HttpResponse, request
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Review


@login_required
@require_POST
def like(request):
    pk = request.POST.get('pk', None)
    object = get_object_or_404(Review, pk=pk)
    user = request.user

    if object.like.filter(id=user.id).exists():
        object.like.remove(user)
        message = '유익해요가 취소되었습니다.'
    else:
        object.like.add(user)
        message = '유익해요를 누르셨습니다.'

    context = {'likes_count':object.like.count(), 'message': message}
    return HttpResponse(json.dumps(context), content_type="application/json")

def fun(request):
    pk = request.POST.get('pk', None)
    object = get_object_or_404(Review, pk=pk)
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
    object = get_object_or_404(Review, pk=pk)
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
    object = get_object_or_404(Review, pk=pk)
    user = request.user

    if object.scrap.filter(id=user.id).exists():
        object.scrap.remove(user)
        message = '스크랩이 취소되었습니다.'
    else:
        object.scrap.add(user)
        message = '스크랩 하셨습니다.'

    context = {'scraps_count':object.scrap.count(), 'message': message}
    return HttpResponse(json.dumps(context), content_type="application/json")