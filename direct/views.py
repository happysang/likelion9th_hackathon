from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from inner_account.models import CustomUser
from django.contrib.auth.decorators import login_required
from direct.models import Message
from review.models import Review
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

@login_required
def Inbox(request):
	messages = Message.get_messages(user=request.user)
	active_direct = None
	directs = None

	if messages:
		message = messages[0]#Users
		active_direct = message['user'].username
		directs = Message.objects.filter(user=request.user, recipient=message['user'])
		directs.update(is_read=True)
		for message in messages:
			if message['user'].username == active_direct:
				message['unread'] = 0

	context = {
		'directs': directs,
		'messages': messages,
		'active_direct': active_direct,
		}

	
	query = request.GET.get("q")
	if query:
		users = CustomUser.objects.filter(Q(username__icontains=query))
		paginator = Paginator(users, 6)
		page_number = request.GET.get('page')
		users_paginator = paginator.get_page(page_number)
		context['users'] = users_paginator

	template = loader.get_template('direct.html')

	return HttpResponse(template.render(context, request))


@login_required
def Directs(request, username):
	user = request.user
	messages = Message.get_messages(user=user)
	active_direct = username
	directs = Message.objects.filter(user=user, recipient__username=username)
	directs.update(is_read=True)
	for message in messages:
		if message['user'].username == username:
			message['unread'] = 0

	context = {
		'directs': directs,
		'messages': messages,
		'active_direct':active_direct,
	}

	query = request.GET.get("q")
	if query:
		users = CustomUser.objects.filter(Q(username__icontains=query))
		paginator = Paginator(users, 6)
		page_number = request.GET.get('page')
		users_paginator = paginator.get_page(page_number)
		context['users'] = users_paginator

	template = loader.get_template('direct.html')

	return HttpResponse(template.render(context, request))


@login_required
def SendDirect(request):
	from_user = request.user
	to_user_username = request.POST.get('to_user')
	body = request.POST.get('body')
	
	if request.method == 'POST':
		to_user = CustomUser.objects.get(username=to_user_username)
		Message.send_message(from_user, to_user, body)
		return redirect('urlinbox')
	else:
		HttpResponseBadRequest()


@login_required
def UserSearch(request):
	query = request.GET.get("q")
	if query:
		users = CustomUser.objects.filter(Q(username__icontains=query))
		paginator = Paginator(users, 6)
		page_number = request.GET.get('page')
		users_paginator = paginator.get_page(page_number)

		context = {
			'users': users_paginator,
		}
	
	template = loader.get_template('direct.html')
	
	return HttpResponse(template.render(context, request))

@login_required
def NewConversation(request, username):
	from_user = request.user
	to_user = CustomUser.objects.get(username=username)
	body = ' '
	if from_user != to_user:
		Message.send_message(from_user, to_user, body)
	return redirect('urlinbox')


def checkDirects(request):
	directs_count = 0
	if request.user.is_authenticated:
		directs_count = Message.objects.filter(user=request.user, is_read=False).count()

	return {'directs_count':directs_count}


def delete(requset , user):
	delete_message = Message.objects.get(sender = user)
	delete_message.delete()
	return redirect('urlinbox')
