from django import forms 
from .models import Qcomment 

class CommentForm(forms.ModelForm): 
    class Meta: 
        model=Qcomment 
        fields=['author_name', 'comment_text','doc']

        labels = {
            'author_name' : '작성자 이름',
            'comment_text' : '댓글'
        }
