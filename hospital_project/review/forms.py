from django import forms 
from .models import Rcomment

class CommentForm(forms.ModelForm): 
    class Meta: 
        model=Rcomment 
        fields=['author_name', 'comment_text', 'doc']

        labels = {
            'author_name' : '작성자 이름',
            'comment_text' : '댓글'
        }

class PostSearchForm(forms.Form) :
    search_word = forms.CharField(label='Search Word')
