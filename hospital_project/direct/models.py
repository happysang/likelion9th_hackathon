from django.db import models
from inner_account.models import CustomUser
from django.db.models import Max

# Create your models here.
class Message(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user')
	sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='from_user')
	recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='to_user')
	body = models.TextField(max_length=1000, blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)
	is_read = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)    
    

	def send_message(from_user, to_user, body):
		sender_message = Message(
			user=from_user,
			sender=from_user,
			recipient=to_user,
			body=body,
			is_read=True)
		sender_message.save()

		recipient_message = Message(
			user=to_user,
			sender=from_user,
			body=body,
			recipient=from_user,)
		recipient_message.save()
		return sender_message

	def get_messages(user):
		#메세지 객체를 받을때 지금 로그인된 유저와 recipient의 값이 일치하는것만 불러오는건가? 이코드 무슨뜻?
		messages = Message.objects.filter(user=user).values('recipient').annotate(last=Max('date')).order_by('-last')
		users = []
		for message in messages:
			users.append({
				'user': CustomUser.objects.get(pk=message['recipient']),
				#??
				'last': message['last'],
				#읽지않은 메세지 개수
				'unread': Message.objects.filter(user=user, recipient__pk=message['recipient'], is_read=False).count()
				})
		return users
