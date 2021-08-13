from .models import Information
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from .forms import CommentForm
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
d_list = ['치과', '피부과', '성형외과', '산부인과', '안과', '내과', '외과', '이비인후과', '정형외과',
            '비뇨기과', '정신건강의학과', '재활의학과', '영상의학과', '소아과', '신경외과', '신경과',
            '마취통증의학과', '가정의학과', '한의원', '그 외']

def info_category_view(request):
    return render (request, 'info_category.html')

def info_readall_view(request, d_num):
    for x in range(len(d_list)):
        if d_num == x:
            infos = Information.objects.all()
            info_list = infos.filter(dept=d_list[x])
            info_all = info_list.order_by("-date")
            d_name = d_list[x]

            paginator = Paginator(info_all,5)
            page = request.GET.get('page')
            posts = paginator.get_page(page)
            
            return render(request,"info_readall.html",{'views_info_all':posts, 'd_num':d_num, 'd_name':d_name},)    


def info_detail_view(request, id):
    info = get_object_or_404(Information,pk= id)
    #조회수 기능
    default_view_count = info.view_count
    info.view_count = default_view_count +1 
    info.save()
    doctor_name = info.user_id.replace("✔️","")
    for x in range(len(d_list)):
        if d_list[x] == info.dept:
            d_num = x
    comment_form=CommentForm()
    if request.method == "POST":
         form=CommentForm(request.POST) 
         if form.is_valid(): 
             comment=form.save(commit=False) 
             if comment.doc == 'doc':
                    comment.author_name = "✔️"+request.POST['author_name']
             comment.post= info
             comment.save() 
         return redirect('urlinfodetail',id)
    return render(request,'info_detail.html',{'views_info':info, 'd_num':d_num, 'comment_form':comment_form, 'doctor_name':doctor_name})


def info_new_view(request, d_num):
    for x in range(len(d_list)):
        if x == d_num:
            d_name = d_list[x]
            break
    return render(request, 'info_new.html', {'d_num':d_num, 'd_name':d_name})

def info_create_view(request, d_num):
    if request.method == 'POST':
        cinfo = Information()
        cinfo.title = request.POST['ctitle']
        cinfo.user_id = request.POST['cuser_id']
        cinfo.dept = request.POST['cdept']
        cinfo.body = request.POST['cbody']
        cinfo.date = timezone.now()
        cinfo.doc = request.POST.get('doc')
        if cinfo.doc == 'doc':
            cinfo.user_id = "✔️"+request.POST['cuser_id']
        cinfo.save()
        return redirect('urlinforeadall', d_num)
    else:
        return render(request,'info_new.html')

def info_edit_view(request, id):
    einfo = Information.objects.get(id = id)
    return render(request, 'info_edit.html', {'views_einfo': einfo})

def info_update_view(request, id):
    uinfo = Information.objects.get(id = id)
    uinfo.title = request.POST['utitle']
    uinfo.user_id = request.POST['uuser_id']
    uinfo.dept = request.POST['udept']
    uinfo.body = request.POST['ubody']
    uinfo.date = timezone.now()
    uinfo.save()
    return redirect('urlinfodetail', uinfo.id)
    
def info_delete_view(request, id):
    dinfo = Information.objects.get(id = id)
    for x in range(len(d_list)):
        if d_list[x] == dinfo.dept:
            d_num = x    
    dinfo.delete()
    return redirect('urlinforeadall', d_num)


def info_search_view(request):
    sinfo = Information.objects.all()
    q = request.POST.get('q', "")
    if q:
        sinfo = sinfo.filter(Q(title__icontains=q) | Q(body__icontains=q))
        c = sinfo.count()
        return render(request, 'info_search.html', {'sinfo':sinfo, 'q':q, 'count':c})
    else:
        return render(request, 'info_search.html')

import json
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Information


@login_required
@require_POST
def like(request):
    pk = request.POST.get('pk', None)
    object = get_object_or_404(Information, pk=pk)
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
    object = get_object_or_404(Information, pk=pk)
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
    object = get_object_or_404(Information, pk=pk)
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
    object = get_object_or_404(Information, pk=pk)
    user = request.user

    if object.scrap.filter(id=user.id).exists():
        object.scrap.remove(user)
        message = '스크랩이 취소되었습니다.'
    else:
        object.scrap.add(user)
        message = '스크랩 하셨습니다.'

    context = {'scraps_count':object.scrap.count(), 'message': message}
    return HttpResponse(json.dumps(context), content_type="application/json")