from django import forms 
from .models import Comment 

class CommentForm(forms.ModelForm): 
    class Meta: 
        model=Comment 
        fields=['author_name', 'comment_text']

        labels = {
            'author_name' : '작성자 이름',
            'comment_text' : '댓글'
        }
