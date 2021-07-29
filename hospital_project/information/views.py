#from hospital_project.hospital_project.settings import TIME_ZONE
from django.shortcuts import render,redirect,get_object_or_404
from .models import Info
from django.utils import timezone 

# Create your views here.
def InfoList(request):
    Infos = Info.objects.all()
    return render(request, 'InfoList.html' , {'Infos':Infos})

def write(request):
    return render(request , 'write.html')

def create(request):
    new_Info = Info()
    new_Info.dept = request.POST['dept']
    new_Info.user_id = request.POST['user_id']
    new_Info.date = timezone.now()
    new_Info.title = request.POST['title']
    new_Info.body = request.POST['body']
    new_Info.save()
    return redirect('urlInfoList')
