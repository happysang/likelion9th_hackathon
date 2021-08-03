from review.models import Review
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

# Create your views here.
def review_category_view(request):
    return render (request, 'review_category.html')


def review_detail_view(request, id):
    review = get_object_or_404(Review,pk= id)
    return render(request,'review_detail.html',{'views_review':review})

def review_readall_view(request):
    review_all = Review.objects.order_by("-date")
    return render(request,"review_readall.html",{'views_review_all':review_all})

def review_new_view(request):
    return render(request, 'review_new.html')

def review_create_view(request):
    if request.method == 'POST':
        creview = Review()
        creview.title = request.POST['ctitle']
        creview.user_id = request.POST['cuser_id']
        creview.hname = request.POST['chname']
        creview.dname = request.POST['cdname']
        creview.dept = request.POST['cdept']
        creview.cert = request.FILES.get('ccert')
        creview.body = request.POST['cbody']
        creview.date = timezone.now()
        creview.save()
        return redirect('urlreviewreadall')
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
    ureview.date = timezone.now()
    ureview.save()
    return redirect('urlreviewdetail', ureview.id)
    
def review_delete_view(request, id):
    dreview = Review.objects.get(id = id)
    dreview.delete()
    return redirect('urlreviewreadall')

import json
from django.http import HttpResponse
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
        message = '좋아요가 취소되었습니다.'
    else:
        object.like.add(user)
        message = '좋아요를 누르셨습니다.'

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