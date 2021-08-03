from django.core import paginator
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from .models import Question
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import CommentForm

# Create your views here.

def qcategory(request):
    return render (request, 'qcategory.html')

def allq(request):
    questions = Question.objects.order_by('-date')
    paginator = Paginator(questions,10)
    page = request.GET.get('page')
    questions = paginator.get_page(page)
    return render(request,'allq.html',{'questions':questions})

def new(request):
    return render(request,'new.html')

def create(request):
    new_question = Question()
    new_question.dept = request.POST['dept']
    new_question.title = request.POST['title']
    new_question.user_id = request.POST['user_id']
    new_question.body = request.POST['body']
    new_question.date = timezone.now()
    new_question.save()
    return redirect('urlnamedetail',new_question.id)

def detail(request,id):
    question = get_object_or_404(Question, pk=id)
    default_view_count = question.view_count
    question.view_count = default_view_count +1 
    question.save()
    return render(request,'qdetail.html',{'question':question})

def edit(request,id):
    edit_question = Question.objects.get(id=id)
    return render(request,'qedit.html',{'question':edit_question})

def update(request,id):
    update_question = Question.objects.get(id=id)
    update_question.title = request.POST['htmltitle']
    update_question.dept = request.POST['htmldept']
    update_question.user_id = request.POST['htmluser_id']
    update_question.body = request.POST['htmlbody']
    update_question.date = timezone.now()
    update_question.save()
    return redirect('urlnamedetail', update_question.id)

def add_comment(request, id): 
    question=get_object_or_404(Question, pk=id) 
    if request.method == "POST":
         form=CommentForm(request.POST) 
         if form.is_valid(): 
             comment=form.save(commit=False) 
             comment.post= question 
             comment.save() 
         return redirect('urlnamedetail',id) 
    else: 
        form=CommentForm() 
    return render(request, 'add_comment.html', {'form':form})


def delete(request,id):
    delete_question = Question.objects.get(id=id)
    delete_question.delete()
    return redirect('urlnameallq')

