from review.models import Review
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

# Create your views here.

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
def video_like(request):
    pk = request.POST.get('pk', None)
    object = get_object_or_404(Review, pk=pk)
    user = request.user

    if object.likes_user.filter(id=user.id).exists():
        object.likes_user.remove(user)
        message = '좋아요 취소'
    else:
        object.likes_user.add(user)
        message = '좋아요'

    context = {'likes_count':object.count_likes_user(), 'message': message}
    return HttpResponse(json.dumps(context), content_type="application/json")