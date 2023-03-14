from .models import Comment, Post, About
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ('post',)
