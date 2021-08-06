#from hospital_project.hospital_project.settings import TIME_ZONE
from django.shortcuts import render,redirect,get_object_or_404
from .models import Info
from django.utils import timezone 

# Create your views here.
def InfoList(request):
    Infos = Info.objects.all()
    return render (request, 'InfoList.html' , {'Infos':Infos})

def write(request):
    return render (request , 'write.html')

def create(request):
    new_Info = Info()
    new_Info.dept = request.POST['dept']
    new_Info.user_id = request.POST['user_id']
    new_Info.date = timezone.now()
    new_Info.title = request.POST['title']
    new_Info.body = request.POST['body']
    new_Info.save()
    return redirect('urlInfoList')

def detail(request, Info_id):
    info_detail = get_object_or_404(Info, pk= Info_id)
    return render (request, 'detail.html', {'info': info_detail})


def edit(request , id):
    edit_info = Info.objects.get(id = id)
    return render(request , 'edit.html' , {'info':edit_info})

def update(request,id):
    update_info = Info.objects.get(id =id)
    update_info.dept = request.POST['dept']
    update_info.user_id = request.POST['user_id']
    update_info.date = timezone.now()
    update_info.title = request.POST['title']
    update_info.body = request.POST['body']
    update_info.save()
    return redirect('urldetail' , update_info.id)

def delete(request , user):
    delete_info = Info.objects.get(user = user)
    delete_info.delete()
    return redirect('urlInfoList')


