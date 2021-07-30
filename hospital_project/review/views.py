from review.models import Review
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

# Create your views here.

def review_detail_view(request,each_id):
    review = get_object_or_404(Review,pk=each_id)
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
        creview.cert = request.FILES['ccert']
        creview.body = request.POST['cbody']
        creview.date = timezone.now()
        creview.save()
        return redirect('urlreviewreadall')
    else:
        return render(request,'review_new.html')



