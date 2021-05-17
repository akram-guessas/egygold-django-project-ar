from django import forms
from .models import Comment

class NowComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','title','body')
